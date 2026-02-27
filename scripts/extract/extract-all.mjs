import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { execSync } from "child_process";
import { decodeMsg } from "remsg";
import { dirname } from "path";

const base = "/mnt/c/Users/henri/Documents/RE-Requiem-CZ";
const outDir = "/tmp/re9-translate/json";

// Find all .msg.23 files
const files = execSync(`find "${base}" -name "*.msg.23"`)
  .toString()
  .trim()
  .split("\n");

let totalStrings = 0;
let totalChars = 0;
const summary = [];

for (const file of files) {
  try {
    const data = readFileSync(file);
    const json = decodeMsg(data);

    const relPath = file.replace(base + "/", "");
    const outPath = outDir + "/" + relPath + ".json";
    mkdirSync(dirname(outPath), { recursive: true });
    writeFileSync(outPath, JSON.stringify(json, null, 2));

    let fileStrings = 0;
    let fileChars = 0;
    for (const entry of json.entries) {
      const en = entry.strings?.en;
      if (en && en.trim()) {
        fileStrings++;
        fileChars += en.length;
      }
    }

    totalStrings += fileStrings;
    totalChars += fileChars;
    summary.push({ file: relPath, entries: json.entries.length, strings: fileStrings, chars: fileChars });
  } catch (err) {
    console.error(`ERROR: ${file}: ${err.message}`);
  }
}

console.log(`\n=== SUMMARY ===`);
console.log(`Files: ${files.length}`);
console.log(`Total English strings: ${totalStrings}`);
console.log(`Total characters: ${totalChars}`);
console.log(`\nPer file:`);
summary.sort((a, b) => b.chars - a.chars);
for (const s of summary) {
  console.log(`  ${s.strings} strings (${s.chars} chars) - ${s.file}`);
}
