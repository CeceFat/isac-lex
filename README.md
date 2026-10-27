# 3GPP 感知標準（ISAC）演進

3GPP TR 23.700-14《Study on Integrated Sensing and Communication; Stage 2》（SA2，Rel-20，v20.0.0，2026 年 3 月核准）的中文拆解。
這份研究報告決定 5G-A「讓基地台兼當雷達」的核心網架構。本站把報告裡 39 個候選方案逐一讀完，把結論每一條追到出處，
再用 SA2 六次會議的會議文件與主席筆記，重建這些方案怎麼被合併、表態與表決。

- 網站：<https://cecefat.github.io/isac-lex/>（入口是給非電機背景讀者的白話圖解）
- 專業版圖表：[時序熱度圖](https://cecefat.github.io/isac-lex/timeline.html)、[演進圖](https://cecefat.github.io/isac-lex/evolution.html)
- 原文：[3GPP Portal](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=4399)、[各版本](https://www.3gpp.org/ftp/Specs/archive/23_series/23.700-14/)、[SA2 會議資料夾](https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/)

| 報告 | 內容 |
|---|---|
| [`reports/plain-language.md`](reports/plain-language.md) | 白話說明：八個爭論，給非電機背景讀者 |
| [`reports/solution-differences.md`](reports/solution-differences.md) | 39 方案技術差異精析：逐一拆到要件，§8 每條結論的原文溯源 |
| [`reports/dispute-analysis.md`](reports/dispute-analysis.md) | 爭點技術路線分析：七個爭點的技術取捨，舉手表決票數與各陣營論據 |
| [`reports/tdoc-heat-and-evolution.md`](reports/tdoc-heat-and-evolution.md) | tdoc 層熱度與演進：693 份會議文件與主席筆記重建的合併、連署與表決過程 |
| [`reports/version-trace.md`](reports/version-trace.md) | 版本溯源：研究報告 10 個版本的逐版比對 |
| [`reports/80211bf-vs-cellular-isac.md`](reports/80211bf-vs-cellular-isac.md) | IEEE 802.11bf（Wi-Fi 感知）對 cellular ISAC 的啟發與影響 |

## 結論先講

- **定案架構**：核心網新設一個 Sensing Function，內部可以分成控制與處理兩部分但不標準化中間介面；
  它對基地台的控制信令與感知資料都走直連，不經 AMF；Rel-20 只讓基地台（gNB）當感知實體。
- **吵最久的是「控制信令要不要經 AMF」**：2025 年 11 月擱置成待決事項，2026 年 2 月舉手表決「只走直連」，
  支持 19、不支持 6、反對 3。
- **39 個方案進場後沒有一個被刪除，也沒有互相合併**；落選的意思是沒寫進 §8 結論。
  分類結果：採納 13、部分採納 8、未決 2、落選 16。
- **手機（UE）相關設計出局，是研究範圍跟著 RAN 的 Rel-20 範圍走，不是技術上被否決**；3GPP 的 6G 架構研究已把 UE 參與列為議題。
- **§8 有幾條結論可以逐字追到來源方案**：撤銷條件來自 #11，「交換連線資訊後直連」來自 #18，請求參數來自 #27 與 #28。
- **還沒解決**：基地台第一次怎麼找到 Sensing Function、識別碼體系、區域怎麼表示、基地台能否回報「做不到」、運算放在基地台還是核心網。

## 這一站不含原文

3GPP 文件 © 3GPP Organizational Partners；IEEE Std 802.11bf-2025 © IEEE，是授權文件。所以：

- **不附任何原文檔案**：TR、會議文件、主席筆記、IEEE PDF 都不在 repo 裡。`source/`（本機抽取的文字，只用於核對）列在 `.gitignore`。
- 引用只限含關鍵詞的短句，用於評論與研究；其餘是用自己的話寫的轉述與分析。
- 每一則引文都附 TR 段落座標（¶）或會議文件編號，讀者可以自己到 3GPP 官方 FTP 下載原文核對。

## 證據紀律

`tools/verify_quotes.py` 把報告裡每一則英文引文（目前 121 則）對原文機械核對，任何一則不通過即回報失敗：

| 規則 | 做法 |
|---|---|
| 附 ¶ 的引文 | 必須出現在所標的 TR 段落（容許前後 2 段）；只出現在 TR 其他地方，視為座標錯誤 |
| 未附 ¶ 的引文 | 必須出現在 TR 正文或表格、TR v0.2.0、TS 22.137、TR 22.870、SA2#173 會議文件、SA2 主席筆記或 IEEE 802.11bf 其中之一 |
| 含省略號的引文 | 逐段核對 |

¶ 是官方 v20.0.0 docx 以 python-docx 列舉的段落索引（含空段落）。
這些核對保證「引文確實印在那裡」，不保證我把它讀對了意思；轉述、分類與推論是判斷。

## 重建

```
python tools/extract_sources.py --tr-v20 23700-14-k00.docx --tr-v020 23700-14-020_MCCclean.docx \
    --ts22137 22137-l00.docx --tr22870 22870-k00.docx \
    --tdocs <SA2#173 會議文件資料夾> --chair <主席筆記資料夾> --ieee 80211bf-2025.pdf
python tools/verify_quotes.py
```

需要 python-docx、pypdf；主席筆記是 .doc 檔，需要 antiword。IEEE 文件是選項，沒有它時 802.11bf 報告的引文會核對失敗。

| 檔 | 作用 |
|---|---|
| `index.html` | 白話圖解（網站入口） |
| `timeline.html` | 時序熱度圖：39 個方案的提出與定案時序 |
| `evolution.html` | 演進圖：被併入的提案 → 39 個方案 → 暫定協議 → 結論 → 表決 |
| `reports/*.md` | 六份分析報告 |
| `tools/extract_sources.py` | 從官方檔案抽出本機核對用的文字（寫入 `source/`） |
| `tools/verify_quotes.py` | 引文機械核對 |

## 限制

- 研究報告不是正式規格。要判斷任何專利是否為標準必要專利，得等 Rel-20 正式規格（Stage 2 TS 與 RAN3 Stage 3）。
- TR 裡的流程圖是圖片，沒有讀；程序以文字步驟為準。
- 「熱度」有兩種看法：同一立場的方案數（代理指標），以及實際表態的公司數。兩者在 AMF 之爭給出相反方向，報告裡有說明。
- 方案 #16 對應 Lenovo 的 S2-2505881，信心中等。
- 6G 研究議題（KI#20）只依會議文件標題判斷，沒有讀原文。
- 中文敘述與分類是 AI 協助整理的詮釋，可能有誤。最終檢閱是使用人自己的責任。
- 不是法律意見。

## 關係聲明

本站不是 3GPP、ETSI 或 IEEE 的出版品，未經其審閱或背書。
流程與驗證規則由我訂定；程式、資料整理與分析初稿由 Claude（AI）撰寫。內容不代表作者任何現任或前任雇主之觀點。

同一套做法的其他站：[Anthropic 就業報告拆解](https://cecefat.github.io/ai-employment-lex/)、
[AI 濫用威脅圖譜](https://cecefat.github.io/ai-misuse-lex/)、
[Claude 系統提示詞演變自學站](https://cecefat.github.io/claude-sysprompt-study/)、
[RLHF 知識圖譜](https://cecefat.github.io/rlhf-lex/)、
[英國 SEP／FRAND 因子知識圖譜](https://cecefat.github.io/ukipo-lex/)。
