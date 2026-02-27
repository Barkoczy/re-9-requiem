// Build release packages for distribution
// Usage: npm run release
// Requires: npm run build must be run first (mod/ directory with built .msg.23 files)
//
// PAK format: RE9 uses version 4.2. REtool (tools/REtool.exe) packs mod/ into a
// re_chunk_000.pak.patch_001.pak that the game loads natively without any mod loader.

import { existsSync, mkdirSync, cpSync, readFileSync, renameSync, rmSync } from "fs";
import { execSync } from "child_process";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));

// --- Configuration ---
const MOD_OUTPUT_DIR =
  process.env.RE9_MOD_OUTPUT ||
  resolve(__dirname, "mod");

const DIST_DIR = resolve(__dirname, "dist");
const INSTALLER_DIR = resolve(__dirname, "installer");
const TOOLS_DIR = resolve(__dirname, "tools");
const VERSION = JSON.parse(readFileSync(resolve(__dirname, "package.json"), "utf8")).version;
const PAK_NAME = `RE9-CZ-Preklad-v${VERSION}.pak`;

// --- Validation ---
const modNatives = resolve(MOD_OUTPUT_DIR, "natives");
if (!existsSync(modNatives)) {
  console.error("ERROR: Build output not found at: " + modNatives);
  console.error("Run 'npm run build' first.");
  process.exit(1);
}

const retool = resolve(TOOLS_DIR, "REtool.exe");
if (!existsSync(retool)) {
  console.error("ERROR: REtool.exe not found at: " + retool);
  process.exit(1);
}

// --- Prepare dist directory ---
if (existsSync(DIST_DIR)) {
  rmSync(DIST_DIR, { recursive: true, force: true });
}
mkdirSync(DIST_DIR, { recursive: true });

console.log(`Building release v${VERSION}...\n`);

// ============================================================================
// 0. Build PAK (RE9 requires v4.2 patch PAK — loose files are not loaded)
// ============================================================================
console.log("--- Building PAK v4.2 ---");

const tempPak = resolve(__dirname, "mod.pak"); // REtool writes to CWD by default
const distPak = resolve(DIST_DIR, PAK_NAME);

try {
  execSync(`"${retool}" -version 4 2 -c "${MOD_OUTPUT_DIR}"`, {
    stdio: "inherit",
    cwd: __dirname,
  });
} catch (_) {
  // REtool exits with code 1 even on success; verify output file instead
}

if (!existsSync(tempPak)) {
  console.error("ERROR: REtool did not produce mod.pak");
  process.exit(1);
}

renameSync(tempPak, distPak);
console.log(`OK: ${distPak}\n`);

// ============================================================================
// 1. Fluffy Mod Manager package (ZIP)
//    Contains pre-built PAK + modinfo.ini. Install: rename to
//    re_chunk_000.pak.patch_001.pak and drop in game root. FluffyMM support
//    will be added once REFramework supports RE9.
// ============================================================================
console.log("--- Fluffy Mod Manager package ---");

const fluffyDir = resolve(DIST_DIR, "fluffy");
const fluffyModDir = resolve(fluffyDir, "RE9-CZ-Preklad");

mkdirSync(fluffyModDir, { recursive: true });

cpSync(distPak, resolve(fluffyModDir, "re_chunk_000.pak.patch_001.pak"));
cpSync(resolve(INSTALLER_DIR, "modinfo.ini"), resolve(fluffyModDir, "modinfo.ini"));

const fluffyZip = resolve(DIST_DIR, `RE9-CZ-Preklad-v${VERSION}-FluffyMM.zip`);
execSync(
  `powershell -NoProfile -Command "Compress-Archive -Path '${fluffyModDir}' -DestinationPath '${fluffyZip}' -Force"`,
  { stdio: "inherit" }
);

console.log(`OK: ${fluffyZip}\n`);

// ============================================================================
// 2. CLI installer package (ZIP)
//    Contains pre-built PAK + install.bat + install.ps1
// ============================================================================
console.log("--- CLI installer package ---");

const cliDir = resolve(DIST_DIR, "cli");
const cliModDir = resolve(cliDir, "RE9-CZ-Preklad");

mkdirSync(cliModDir, { recursive: true });

cpSync(distPak, resolve(cliModDir, "re9-cz-preklad.pak"));
cpSync(resolve(INSTALLER_DIR, "install.bat"), resolve(cliModDir, "install.bat"));
cpSync(resolve(INSTALLER_DIR, "install.ps1"), resolve(cliModDir, "install.ps1"));

const cliZip = resolve(DIST_DIR, `RE9-CZ-Preklad-v${VERSION}-CLI.zip`);
execSync(
  `powershell -NoProfile -Command "Compress-Archive -Path '${cliModDir}' -DestinationPath '${cliZip}' -Force"`,
  { stdio: "inherit" }
);

console.log(`OK: ${cliZip}\n`);

// ============================================================================
// 3. Inno Setup input (ready to compile with ISCC.exe)
// ============================================================================
console.log("--- Inno Setup input ---");

const innoDir = resolve(DIST_DIR, "inno");

mkdirSync(innoDir, { recursive: true });

cpSync(distPak, resolve(innoDir, "re9-cz-preklad.pak"));
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
console.log(`  ${PAK_NAME}                          — patch PAK (RE9 v4.2)`);
console.log(`  RE9-CZ-Preklad-v${VERSION}-FluffyMM.zip  — Fluffy Mod Manager`);
console.log(`  RE9-CZ-Preklad-v${VERSION}-CLI.zip        — CLI installer (bat/ps1)`);
console.log(`  inno/                              — ISCC.exe → .exe installer`);
