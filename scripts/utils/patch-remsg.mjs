// Patch remsg encode.mjs:
//   1) uint64/int32 mismatch bug (see patches/remsg-encode-uint64.md)
//   2) setString("GMSG") writes 5 bytes (GMSG+NUL) but decoder reads only 4
import { readFileSync, writeFileSync } from "fs";

const file = "node_modules/remsg/dist/encode.mjs";
let src = readFileSync(file, "utf8");
let changed = false;

// --- Patch 1: uint64 encode bug ---
const buggy1 = `case 0:
					encoder.setInt32(entry.attributes[j]);
					break;`;

const fixed1 = `case 0: {
					const v = entry.attributes[j];
					if (Number.isSafeInteger(v)) {
						encoder.setInt64(BigInt(v));
					} else {
						encoder.setInt64(-1n);
					}
					break;
				}`;

if (src.includes("setInt32(entry.attributes")) {
  src = src.replace(buggy1, fixed1);
  changed = true;
  console.log("PATCHED: remsg encode.mjs (uint64 fix applied)");
} else if (src.includes("setInt64(BigInt(v))")) {
  console.log("OK: remsg encode.mjs uint64 already patched");
} else {
  console.error("WARNING: Could not find uint64 patch target in encode.mjs");
  process.exit(1);
}

// --- Patch 2: setString("GMSG") writes null terminator (5 bytes, decoder expects 4) ---
if (src.includes('encoder.setString("GMSG")')) {
  src = src.replace('encoder.setString("GMSG")', 'encoder.setBuffer(Buffer.from("GMSG"))');
  // ensure Buffer import is present
  if (!src.includes('import { Buffer }') && !src.includes("import {Buffer}")) {
    src = 'import { Buffer } from "node:buffer";\n' + src;
  }
  changed = true;
  console.log("PATCHED: remsg encode.mjs (GMSG magic 4-byte fix applied)");
} else if (src.includes('encoder.setBuffer(Buffer.from("GMSG"))')) {
  console.log("OK: remsg encode.mjs GMSG already patched");
} else {
  console.error("WARNING: Could not find GMSG patch target in encode.mjs");
  process.exit(1);
}

// --- Patch 3: attributeValues offset captured AFTER write (off by 8 bytes) ---
// The offset must be captured BEFORE writing the placeholder value.
const buggy3 = `\t\t\tswitch (input.meta.attributes[j].type) {
\t\t\t\tcase -1:
\t\t\t\t\tencoder.setInt64(-1n);
\t\t\t\t\tbreak;
\t\t\t\tcase 0: {
\t\t\t\t\tconst v = entry.attributes[j];
\t\t\t\t\tif (Number.isSafeInteger(v)) {
\t\t\t\t\t\tencoder.setInt64(BigInt(v));
\t\t\t\t\t} else {
\t\t\t\t\t\tencoder.setInt64(-1n);
\t\t\t\t\t}
\t\t\t\t\tbreak;
\t\t\t\t}
\t\t\t\tcase 1:
\t\t\t\t\tencoder.setDouble(entry.attributes[j]);
\t\t\t\t\tbreak;
\t\t\t\tcase 2:
\t\t\t\t\tencoder.setInt64(-1n);
\t\t\t\t\tbreak;
\t\t\t}
\t\t\tentryHeaderOffsets[i].attributeValues[j] = encoder.currentOffset;`;

const fixed3 = `\t\t\tentryHeaderOffsets[i].attributeValues[j] = encoder.currentOffset;
\t\t\tswitch (input.meta.attributes[j].type) {
\t\t\t\tcase -1:
\t\t\t\t\tencoder.setInt64(-1n);
\t\t\t\t\tbreak;
\t\t\t\tcase 0: {
\t\t\t\t\tconst v = entry.attributes[j];
\t\t\t\t\tif (Number.isSafeInteger(v)) {
\t\t\t\t\t\tencoder.setInt64(BigInt(v));
\t\t\t\t\t} else {
\t\t\t\t\t\tencoder.setInt64(-1n);
\t\t\t\t\t}
\t\t\t\t\tbreak;
\t\t\t\t}
\t\t\t\tcase 1:
\t\t\t\t\tencoder.setDouble(entry.attributes[j]);
\t\t\t\t\tbreak;
\t\t\t\tcase 2:
\t\t\t\t\tencoder.setInt64(-1n);
\t\t\t\t\tbreak;
\t\t\t}`;

if (src.includes("entryHeaderOffsets[i].attributeValues[j] = encoder.currentOffset;")) {
  if (src.includes(buggy3)) {
    src = src.replace(buggy3, fixed3);
    changed = true;
    console.log("PATCHED: remsg encode.mjs (attributeValues offset-before-write fix applied)");
  } else {
    console.log("OK: remsg encode.mjs attributeValues already patched");
  }
} else {
  console.error("WARNING: Could not find attributeValues patch target in encode.mjs");
  process.exit(1);
}

if (changed) writeFileSync(file, src);
