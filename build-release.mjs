// Build release packages for distribution
// Usage: npm run release
// Requires: npm run build must be run first (mod/ directory with built .msg.23 files)

import { existsSync, mkdirSync, cpSync, readFileSync, writeFileSync } from "fs";
import { execSync } from "child_process";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));

// --- Configuration ---
const MOD_OUTPUT_DIR =
  process.env.RE9_MOD_OUTPUT ||
  "/mnt/c/Users/henri/Documents/RE-Requiem-CZ/mod";

const DIST_DIR = resolve(__dirname, "dist");
const INSTALLER_DIR = resolve(__dirname, "installer");
const VERSION = JSON.parse(readFileSync(resolve(__dirname, "package.json"), "utf8")).version;

// --- Validation ---
const modNatives = resolve(MOD_OUTPUT_DIR, "natives");
if (!existsSync(modNatives)) {
  console.error("ERROR: Build output not found at: " + modNatives);
  console.error("Run 'npm run build' first.");
  process.exit(1);
}

// --- Prepare dist directory ---
if (existsSync(DIST_DIR)) {
  execSync(`rm -rf "${DIST_DIR}"`);
}
mkdirSync(DIST_DIR, { recursive: true });

console.log(`Building release v${VERSION}...\n`);

// ============================================================================
// 1. Fluffy Mod Manager package (ZIP)
// ============================================================================
console.log("--- Fluffy Mod Manager package ---");

const fluffyDir = resolve(DIST_DIR, "fluffy");
const fluffyModDir = resolve(fluffyDir, "RE9-CZ-Preklad");

mkdirSync(fluffyModDir, { recursive: true });

// Copy natives/
cpSync(modNatives, resolve(fluffyModDir, "natives"), { recursive: true });

// Copy modinfo.ini
cpSync(resolve(INSTALLER_DIR, "modinfo.ini"), resolve(fluffyModDir, "modinfo.ini"));

// Create ZIP
const fluffyZip = resolve(DIST_DIR, `RE9-CZ-Preklad-v${VERSION}-FluffyMM.zip`);
execSync(`cd "${fluffyDir}" && zip -r "${fluffyZip}" RE9-CZ-Preklad/`, { stdio: "inherit" });

console.log(`OK: ${fluffyZip}\n`);

// ============================================================================
// 2. CLI installer package (ZIP)
// ============================================================================
console.log("--- CLI installer package ---");

const cliDir = resolve(DIST_DIR, "cli");
const cliModDir = resolve(cliDir, "RE9-CZ-Preklad");

mkdirSync(cliModDir, { recursive: true });

// Copy natives/
cpSync(modNatives, resolve(cliModDir, "natives"), { recursive: true });

// Copy CLI installer scripts
cpSync(resolve(INSTALLER_DIR, "install.bat"), resolve(cliModDir, "install.bat"));
cpSync(resolve(INSTALLER_DIR, "install.ps1"), resolve(cliModDir, "install.ps1"));

// Create ZIP
const cliZip = resolve(DIST_DIR, `RE9-CZ-Preklad-v${VERSION}-CLI.zip`);
execSync(`cd "${cliDir}" && zip -r "${cliZip}" RE9-CZ-Preklad/`, { stdio: "inherit" });

console.log(`OK: ${cliZip}\n`);

// ============================================================================
// 3. Inno Setup input (ready to compile with ISCC.exe)
// ============================================================================
console.log("--- Inno Setup input ---");

const innoDir = resolve(DIST_DIR, "inno");

mkdirSync(innoDir, { recursive: true });

// Copy natives/
cpSync(modNatives, resolve(innoDir, "natives"), { recursive: true });

// Copy Inno Setup files
cpSync(resolve(INSTALLER_DIR, "re9-cz-mod.iss"), resolve(innoDir, "re9-cz-mod.iss"));
cpSync(resolve(INSTALLER_DIR, "info-before.rtf"), resolve(innoDir, "info-before.rtf"));
cpSync(resolve(INSTALLER_DIR, "icon.ico"), resolve(innoDir, "icon.ico"));
cpSync(resolve(__dirname, "LICENSE"), resolve(innoDir, "LICENSE"));

console.log(`OK: ${innoDir}`);
console.log(`    Compile on Windows: ISCC.exe re9-cz-mod.iss`);
console.log(`    Output: RE9-CZ-Preklad-v${VERSION}-Setup.exe\n`);

// ============================================================================
// Summary
// ============================================================================
console.log("=== Release v" + VERSION + " ready ===");
console.log("dist/");
console.log(`  ${`RE9-CZ-Preklad-v${VERSION}-FluffyMM.zip`}  — Fluffy Mod Manager`);
console.log(`  ${`RE9-CZ-Preklad-v${VERSION}-CLI.zip`}        — CLI installer (bat/ps1)`);
console.log(`  inno/                              — ISCC.exe → .exe installer`);
