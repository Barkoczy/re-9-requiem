import { readFileSync, writeFileSync } from "fs";
import { decodeMsg } from "remsg";

const file = process.argv[2];
if (!file) {
  console.error("Usage: node extract.mjs <file.msg.23>");
  process.exit(1);
}

const data = readFileSync(file);
const json = decodeMsg(data);

// Output the JSON to see the structure
writeFileSync(file + ".json", JSON.stringify(json, null, 2));
console.log(`Decoded ${file} -> ${file}.json`);
console.log(`Entries: ${json.entries?.length ?? "unknown"}`);
