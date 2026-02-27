// Build modified MSG files with Czech translations replacing Polish
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "fs";
import { execSync } from "child_process";
import { decodeMsg, encodeMsg } from "remsg";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));

// --- Configuration -----------------------------------------------------------
// Path to the original game data (extracted PAK with .msg.23 files)
const GAME_DATA_DIR =
  process.env.RE9_GAME_DATA ||
  "/mnt/c/Users/henri/Documents/RE-Requiem-CZ";

// Path where built mod files are written
const MOD_OUTPUT_DIR =
  process.env.RE9_MOD_OUTPUT ||
  "/mnt/c/Users/henri/Documents/RE-Requiem-CZ/mod";
// -----------------------------------------------------------------------------

const translationsDir = resolve(__dirname, "translations");

// Find all translation files
const files = execSync(`find "${translationsDir}" -name "*.json"`)
  .toString()
  .trim()
  .split("\n")
  .filter(Boolean);

let totalReplaced = 0;
let totalFiles = 0;
let skipped = 0;
let errors = 0;

for (const transFile of files) {
  try {
    const relPath = transFile.replace(translationsDir + "/", "");
    const msgRelPath = relPath.replace(".json", "");
    const origMsgFile = GAME_DATA_DIR + "/" + msgRelPath;

    if (!existsSync(origMsgFile)) {
      console.error(`MISS: ${origMsgFile}`);
      errors++;
      continue;
    }

    // Read original MSG
    const origData = readFileSync(origMsgFile);
    const msg = decodeMsg(origData);

    // Skip files with no entries
    if (!msg.entries || msg.entries.length === 0) {
      console.log(`SKIP: ${msgRelPath} (no entries)`);
      skipped++;
      continue;
    }

    // Read translations
    const translations = JSON.parse(readFileSync(transFile, "utf8"));

    // Apply translations - replace PL slot with Czech text
    let replaced = 0;
    for (const entry of msg.entries) {
      const czText = translations[entry.name];
      if (czText && entry.strings) {
        entry.strings.pl = czText;
        replaced++;
      }
    }

    // Encode back to MSG
    const outPath = MOD_OUTPUT_DIR + "/" + msgRelPath;
    mkdirSync(dirname(outPath), { recursive: true });
    const encoded = encodeMsg(msg);
    writeFileSync(outPath, Buffer.from(encoded));

    totalReplaced += replaced;
    totalFiles++;
    console.log(`OK: ${msgRelPath} (${replaced} strings replaced)`);
  } catch (err) {
    console.error(`ERROR: ${transFile}: ${err.message}`);
    errors++;
  }
}

console.log(`\nDone! ${totalFiles} files built, ${totalReplaced} strings replaced`);
console.log(`Skipped: ${skipped}, Errors: ${errors}`);
console.log(`Output: ${MOD_OUTPUT_DIR}`);
