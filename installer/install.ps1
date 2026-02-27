# RE9 Requiem - Czech Translation Mod Installer
# Requires: Windows 10/11, PowerShell 5.1+

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

[System.Windows.Forms.Application]::EnableVisualStyles()

# --- Constants ---
$DEFAULT_GAME_PATH = "C:\Program Files (x86)\Steam\steamapps\common\RESIDENT EVIL requiem BIOHAZARD requiem"
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
$NATIVES_SOURCE = Join-Path $SCRIPT_DIR "natives"
$WINDOW_TITLE = "RE9: Requiem — Český překlad"

# --- Validation ---
function Test-GameDirectory {
    param([string]$Path)

    if (-not (Test-Path $Path)) {
        return @{ Valid = $false; Reason = "Adresář neexistuje." }
    }

    # RE Engine games contain .pak data archives
    $pakFiles = Get-ChildItem -Path $Path -Filter "re_chunk_*.pak" -ErrorAction SilentlyContinue
    if ($pakFiles.Count -eq 0) {
        return @{ Valid = $false; Reason = "Nenalezeny herní soubory (re_chunk_*.pak).`nToto není kořenový adresář hry RE Engine." }
    }

    return @{ Valid = $true; Reason = "" }
}

function Test-ModSource {
    if (-not (Test-Path $NATIVES_SOURCE)) {
        return $false
    }
    $msgFiles = Get-ChildItem -Path $NATIVES_SOURCE -Filter "*.msg.23" -Recurse -ErrorAction SilentlyContinue
    return ($msgFiles.Count -gt 0)
}

# --- GUI ---
$form = New-Object System.Windows.Forms.Form
$form.Text = $WINDOW_TITLE
$form.Size = New-Object System.Drawing.Size(560, 340)
$form.StartPosition = "CenterScreen"
$form.FormBorderStyle = "FixedDialog"
$form.MaximizeBox = $false
$form.Font = New-Object System.Drawing.Font("Segoe UI", 9)

# Title label
$lblTitle = New-Object System.Windows.Forms.Label
$lblTitle.Text = "Instalace českého překladu"
$lblTitle.Font = New-Object System.Drawing.Font("Segoe UI", 14, [System.Drawing.FontStyle]::Bold)
$lblTitle.Location = New-Object System.Drawing.Point(20, 15)
$lblTitle.Size = New-Object System.Drawing.Size(500, 30)
$form.Controls.Add($lblTitle)

$lblDesc = New-Object System.Windows.Forms.Label
$lblDesc.Text = "Mod nahradí polský jazykový slot českým textem.`nPo instalaci zvolte v nastavení hry Jazyk → Polski."
$lblDesc.Location = New-Object System.Drawing.Point(20, 50)
$lblDesc.Size = New-Object System.Drawing.Size(500, 35)
$form.Controls.Add($lblDesc)

# Path group
$lblPath = New-Object System.Windows.Forms.Label
$lblPath.Text = "Cílový adresář hry:"
$lblPath.Location = New-Object System.Drawing.Point(20, 100)
$lblPath.Size = New-Object System.Drawing.Size(500, 20)
$form.Controls.Add($lblPath)

$txtPath = New-Object System.Windows.Forms.TextBox
$txtPath.Location = New-Object System.Drawing.Point(20, 122)
$txtPath.Size = New-Object System.Drawing.Size(415, 24)
$txtPath.Text = $DEFAULT_GAME_PATH
$form.Controls.Add($txtPath)

$btnBrowse = New-Object System.Windows.Forms.Button
$btnBrowse.Text = "Procházet..."
$btnBrowse.Location = New-Object System.Drawing.Point(440, 121)
$btnBrowse.Size = New-Object System.Drawing.Size(90, 25)
$form.Controls.Add($btnBrowse)

# Status label
$lblStatus = New-Object System.Windows.Forms.Label
$lblStatus.Text = ""
$lblStatus.Location = New-Object System.Drawing.Point(20, 160)
$lblStatus.Size = New-Object System.Drawing.Size(500, 60)
$form.Controls.Add($lblStatus)

# Progress bar
$progressBar = New-Object System.Windows.Forms.ProgressBar
$progressBar.Location = New-Object System.Drawing.Point(20, 225)
$progressBar.Size = New-Object System.Drawing.Size(510, 22)
$progressBar.Visible = $false
$form.Controls.Add($progressBar)

# Buttons
$btnInstall = New-Object System.Windows.Forms.Button
$btnInstall.Text = "Instalovat"
$btnInstall.Location = New-Object System.Drawing.Point(340, 260)
$btnInstall.Size = New-Object System.Drawing.Size(90, 30)
$form.Controls.Add($btnInstall)

$btnClose = New-Object System.Windows.Forms.Button
$btnClose.Text = "Zavřít"
$btnClose.Location = New-Object System.Drawing.Point(440, 260)
$btnClose.Size = New-Object System.Drawing.Size(90, 30)
$form.Controls.Add($btnClose)

# --- Events ---
$btnBrowse.Add_Click({
    $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $dialog.Description = "Vyberte kořenový adresář hry RE9: Requiem"
    $dialog.SelectedPath = $txtPath.Text
    if ($dialog.ShowDialog() -eq "OK") {
        $txtPath.Text = $dialog.SelectedPath
    }
})

$btnClose.Add_Click({
    $form.Close()
})

$btnInstall.Add_Click({
    $lblStatus.ForeColor = [System.Drawing.Color]::Black
    $lblStatus.Text = "Ověřuji..."
    $form.Refresh()

    # Check mod source files
    if (-not (Test-ModSource)) {
        $lblStatus.ForeColor = [System.Drawing.Color]::Red
        $lblStatus.Text = "Chyba: Složka 'natives' s přeloženými soubory nebyla nalezena`nvedle instalátoru. Zkontrolujte úplnost stažených souborů."
        return
    }

    # Validate game directory
    $check = Test-GameDirectory -Path $txtPath.Text
    if (-not $check.Valid) {
        $lblStatus.ForeColor = [System.Drawing.Color]::Red
        $lblStatus.Text = "Chyba: $($check.Reason)"
        return
    }

    # Confirm overwrite if natives already exists in game dir
    $targetNatives = Join-Path $txtPath.Text "natives\stm\message"
    if (Test-Path $targetNatives) {
        $confirm = [System.Windows.Forms.MessageBox]::Show(
            "V herním adresáři již existují modifikované soubory.`nPřepsat?",
            "Potvrzení",
            [System.Windows.Forms.MessageBoxButtons]::YesNo,
            [System.Windows.Forms.MessageBoxIcon]::Question
        )
        if ($confirm -ne "Yes") {
            $lblStatus.Text = "Instalace zrušena."
            return
        }
    }

    # Copy files
    $btnInstall.Enabled = $false
    $btnBrowse.Enabled = $false
    $txtPath.Enabled = $false
    $progressBar.Visible = $true
    $progressBar.Style = "Marquee"
    $lblStatus.Text = "Kopíruji soubory..."
    $form.Refresh()

    try {
        $files = Get-ChildItem -Path $NATIVES_SOURCE -Recurse -File
        $total = $files.Count
        $progressBar.Style = "Continuous"
        $progressBar.Minimum = 0
        $progressBar.Maximum = $total
        $progressBar.Value = 0
        $copied = 0

        foreach ($file in $files) {
            $relativePath = $file.FullName.Substring($SCRIPT_DIR.Length + 1)
            $destPath = Join-Path $txtPath.Text $relativePath
            $destDir = Split-Path -Parent $destPath

            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            }

            Copy-Item -Path $file.FullName -Destination $destPath -Force
            $copied++
            $progressBar.Value = $copied
            if ($copied % 10 -eq 0) { $form.Refresh() }
        }

        $progressBar.Value = $total
        $lblStatus.ForeColor = [System.Drawing.Color]::DarkGreen
        $lblStatus.Text = "Instalace dokončena! Zkopírováno $copied souborů.`nV nastavení hry zvolte: Jazyk → Polski"

        [System.Windows.Forms.MessageBox]::Show(
            "Český překlad byl úspěšně nainstalován!`n`nZkopírováno: $copied souborů`n`nV nastavení hry zvolte:`nJazyk → Polski",
            "Hotovo",
            [System.Windows.Forms.MessageBoxButtons]::OK,
            [System.Windows.Forms.MessageBoxIcon]::Information
        ) | Out-Null
    }
    catch {
        $lblStatus.ForeColor = [System.Drawing.Color]::Red
        $lblStatus.Text = "Chyba při kopírování: $($_.Exception.Message)"
    }
    finally {
        $btnInstall.Enabled = $true
        $btnBrowse.Enabled = $true
        $txtPath.Enabled = $true
    }
})

# Auto-check default path on load
$form.Add_Shown({
    if (Test-Path $DEFAULT_GAME_PATH) {
        $lblStatus.ForeColor = [System.Drawing.Color]::DarkGreen
        $lblStatus.Text = "Hra nalezena na výchozí cestě."
    } else {
        $lblStatus.ForeColor = [System.Drawing.Color]::DarkOrange
        $lblStatus.Text = "Výchozí cesta nenalezena. Zadejte cestu k hernímu adresáři."
    }
})

$form.ShowDialog() | Out-Null
