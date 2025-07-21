$hashFiles = @(
    # content_analyser
    @{name="nsfw_1"; ver="models-3.3.0"},
    @{name="nsfw_2"; ver="models-3.3.0"},
    @{name="nsfw_3"; ver="models-3.3.0"},
    # face_detector
    @{name="retinaface_10g"; ver="models-3.0.0"},
    @{name="scrfd_2.5g"; ver="models-3.0.0"},
    @{name="yoloface_8n"; ver="models-3.0.0"},
    # face_landmarker
    @{name="2dfan4"; ver="models-3.0.0"},
    @{name="peppa_wutz"; ver="models-3.0.0"},
    @{name="fan_68_5"; ver="models-3.0.0"},
    # face_masker
    @{name="xseg_1"; ver="models-3.1.0"},
    @{name="xseg_2"; ver="models-3.1.0"},
    # face_recognizer
    @{name="arcface_w600k_r50"; ver="models-3.0.0"},
    # voice_extractor
    @{name="kim_vocal_2"; ver="models-3.0.0"},
    # face_enhancer
    @{name="codeformer"; ver="models-3.0.0"},
    @{name="gfpgan_1.2"; ver="models-3.0.0"},
    @{name="gfpgan_1.3"; ver="models-3.0.0"},
    # face_swapper
    @{name="blendswap_256"; ver="models-3.0.0"},
    @{name="ghost_1_256"; ver="models-3.0.0"},
    @{name="arcface_converter_ghost"; ver="models-3.0.0"},
    # lip_syncer
    @{name="edtalk_256"; ver="models-3.3.0"},
    @{name="wav2lip_96"; ver="models-3.0.0"},
    @{name="wav2lip_gan_96"; ver="models-3.0.0"}
)
$targetDir = "facefusion/.assets/models"
if (!(Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force }
foreach ($file in $hashFiles) {
    foreach ($ext in @(".hash", ".onnx")) {
        $url = "https://github.com/facefusion/facefusion-assets/releases/download/$($file.ver)/$($file.name)$ext"
        $out = "$targetDir/$($file.name)$ext"
        Write-Host "Downloading $($file.name)$ext ..."
        try {
            Invoke-WebRequest -Uri $url -OutFile $out -ErrorAction Stop
        } catch {
            Write-Host "Failed to download $($file.name)$ext from $url"
        }
    }
}
Write-Host "Essential hash and onnx files downloaded." 