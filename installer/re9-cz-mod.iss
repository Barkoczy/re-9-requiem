; RE9: Requiem - Czech Translation Mod - Inno Setup 6 Installer Script
; Compile with: ISCC.exe re9-cz-mod.iss
; Requires: Inno Setup 6.x (https://jrsoftware.org/isinfo.php)

#define MyAppName "RE9 Requiem - Cesky preklad"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Barkoczy"
#define MyAppURL "https://github.com/Barkoczy/re-9-requiem"
#define SteamAppId "3764200"
#define GameDirName "RESIDENT EVIL requiem BIOHAZARD requiem"

[Setup]
AppId={{B7E3F2A1-9C4D-4E8B-A6F5-1D2C3B4A5E6F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}/issues
DefaultDirName={code:GetDefaultDir}
DirExistsWarning=no
DisableProgramGroupPage=yes
OutputBaseFilename=RE9-CZ-Preklad-v{#MyAppVersion}-Setup
SetupIconFile=icon.ico
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
WizardSizePercent=110
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
Uninstallable=yes
UninstallFilesDir={app}\re9-cz-mod-uninstall
CreateUninstallRegKey=yes
LicenseFile=LICENSE
InfoBeforeFile=info-before.rtf

[Languages]
Name: "czech"; MessagesFile: "compiler:Languages\Czech.isl"

[Files]
Source: "natives\*"; DestDir: "{app}\natives"; Flags: ignoreversion recursesubdirs createallsubdirs

[Messages]
czech.SelectDirLabel3=Vyberte korenovy adresar hry {#GameDirName}.
czech.SelectDirBrowseLabel=Instalator automaticky detekoval cestu ke hre ze Steam registru.%nPokud cesta neni spravna, kliknte na Prochazet a vyberte spravny adresar.

[Code]

// --- Steam game path auto-detection ---

function GetSteamInstallPath(): String;
var
  SteamPath: String;
begin
  Result := '';

  // Try Steam registry (HKLM 64-bit uninstall entry)
  if RegQueryStringValue(HKLM,
    'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App {#SteamAppId}',
    'InstallLocation', SteamPath) then
  begin
    if DirExists(SteamPath) then
    begin
      Log('Detected game path from HKLM uninstall registry: ' + SteamPath);
      Result := SteamPath;
      Exit;
    end;
  end;

  // Try HKLM 32-bit view (WOW6432Node)
  if RegQueryStringValue(HKLM32,
    'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App {#SteamAppId}',
    'InstallLocation', SteamPath) then
  begin
    if DirExists(SteamPath) then
    begin
      Log('Detected game path from HKLM32 registry: ' + SteamPath);
      Result := SteamPath;
      Exit;
    end;
  end;

  // Try HKCU (some Steam configs write here)
  if RegQueryStringValue(HKCU,
    'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App {#SteamAppId}',
    'InstallLocation', SteamPath) then
  begin
    if DirExists(SteamPath) then
    begin
      Log('Detected game path from HKCU registry: ' + SteamPath);
      Result := SteamPath;
      Exit;
    end;
  end;
end;

function GetDefaultSteamLibraryPath(): String;
begin
  Result := '';

  // Common default Steam library paths
  if DirExists('C:\Program Files (x86)\Steam\steamapps\common\{#GameDirName}') then
    Result := 'C:\Program Files (x86)\Steam\steamapps\common\{#GameDirName}'
  else if DirExists('D:\SteamLibrary\steamapps\common\{#GameDirName}') then
    Result := 'D:\SteamLibrary\steamapps\common\{#GameDirName}'
  else if DirExists('E:\SteamLibrary\steamapps\common\{#GameDirName}') then
    Result := 'E:\SteamLibrary\steamapps\common\{#GameDirName}'
  else if DirExists('D:\Steam\steamapps\common\{#GameDirName}') then
    Result := 'D:\Steam\steamapps\common\{#GameDirName}'
  else if DirExists('E:\Steam\steamapps\common\{#GameDirName}') then
    Result := 'E:\Steam\steamapps\common\{#GameDirName}';
end;

function GetDefaultDir(Param: String): String;
var
  DetectedPath: String;
begin
  // Priority 1: Steam registry
  DetectedPath := GetSteamInstallPath();
  if DetectedPath <> '' then
  begin
    Result := DetectedPath;
    Exit;
  end;

  // Priority 2: Common Steam library paths
  DetectedPath := GetDefaultSteamLibraryPath();
  if DetectedPath <> '' then
  begin
    Result := DetectedPath;
    Exit;
  end;

  // Fallback: default path
  Result := 'C:\Program Files (x86)\Steam\steamapps\common\{#GameDirName}';
end;

// --- Game directory validation ---

function IsValidGameDirectory(const Dir: String): Boolean;
var
  FindRec: TFindRec;
begin
  Result := False;

  // Check for re_chunk_*.pak files (standard RE Engine data archives)
  if FindFirst(Dir + '\re_chunk_*.pak', FindRec) then
  begin
    Result := True;
    FindClose(FindRec);
    Log('Valid RE Engine game directory confirmed: ' + Dir);
  end;
end;

function NextButtonClick(CurPageID: Integer): Boolean;
var
  SelectedDir: String;
begin
  Result := True;

  if CurPageID = wpSelectDir then
  begin
    SelectedDir := WizardDirValue();

    if not DirExists(SelectedDir) then
    begin
      MsgBox(
        'Zadany adresar neexistuje:' + #13#10 +
        SelectedDir + #13#10#13#10 +
        'Vyberte prosim korenovy adresar hry RE9: Requiem.',
        mbError, MB_OK);
      Result := False;
      Exit;
    end;

    if not IsValidGameDirectory(SelectedDir) then
    begin
      if MsgBox(
        'V adresari nebyly nalezeny herni soubory RE Engine (re_chunk_*.pak).' + #13#10#13#10 +
        'Vybrany adresar:' + #13#10 +
        SelectedDir + #13#10#13#10 +
        'Toto nemusi byt korenovy adresar hry.' + #13#10 +
        'Chcete presto pokracovat v instalaci?',
        mbConfirmation, MB_YESNO) = IDNO then
      begin
        Result := False;
        Exit;
      end;
    end;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  FileCount: Integer;
  FindRec: TFindRec;
begin
  if CurStep = ssPostInstall then
  begin
    // Count installed .msg.23 files for verification
    FileCount := 0;
    if FindFirst(ExpandConstant('{app}\natives\stm\message\dialog\*.msg.23'), FindRec) then
    begin
      repeat
        FileCount := FileCount + 1;
      until not FindNext(FindRec);
      FindClose(FindRec);
    end;
    Log('Installed dialog .msg.23 files: ' + IntToStr(FileCount));
  end;
end;
