// Patch remsg encode.mjs to fix uint64/int32 mismatch bug
// See patches/remsg-encode-uint64.md for details
import { readFileSync, writeFileSync } from "fs";

const file = "node_modules/remsg/dist/encode.mjs";
let src = readFileSync(file, "utf8");

const buggy = `case 0:
					encoder.setInt32(entry.attributes[j]);
					break;`;

const fixed = `case 0: {
					const v = entry.attributes[j];
					if (Number.isSafeInteger(v)) {
						encoder.setInt64(BigInt(v));
					} else {
						encoder.setInt64(-1n);
					}
					break;
				}`;

if (src.includes("setInt32(entry.attributes")) {
  src = src.replace(buggy, fixed);
  writeFileSync(file, src);
  console.log("PATCHED: remsg encode.mjs (uint64 fix applied)");
} else if (src.includes("setInt64(BigInt(v))")) {
  console.log("OK: remsg encode.mjs already patched");
} else {
  console.error("WARNING: Could not find expected code in encode.mjs");
  process.exit(1);
}
