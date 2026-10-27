# TR 23.700-14 的 tdoc 層熱度與演進分析

- 日期：2026-10-27
- 資料：SA2#168–#173 共 6 份 TdocsByAgenda，位於 3GPP 官方 FTP 各會議資料夾（<https://www.3gpp.org/ftp/tsg_sa/WG2_Arch/>，TSGS2_168 至 TSGS2_173）
- 範圍：工作項目 FS_Sensing_ARC 的全部 693 份會議文件（P-CR 643 份），以 TdocsByAgenda 為準；主席筆記另列 10 份，見 §1 第 5 點
- 搭配圖表：[演進圖](https://cecefat.github.io/isac-lex/evolution.html)
- 前置報告：[版本溯源報告](version-trace.md)（TR 版本層）
- 更正：2026-10-27 依簡報包稽核，並以主席筆記交叉核對，更正多項數字，見 §7。

## 0. 結論先講

1. **solution 之間沒有互相合併。** 39 個 solution 進場後各自獨立，沒有一個被併入另一個。真正的「併入」發生在進場**之前**和**之後**兩個時點：
   - **進場前**：3 件 tdoc 正式併入（Rakuten/NIST → #3、ETRI → #22、Xiaomi 撤銷方案 → 既有 #11），另外 4 家公司自己的 KI#1 架構方案沒被處理，也連署了 #3（其中 OPPO、ZTE 在 SA2#170 又提了自己的架構方案）。
   - **進場後**：各公司把立場改寫成「結論提案」。SA2#171、#172 每個 KI 每次會議收到 7～19 份；除了 #171 的 KI#5、KI#6 整組延到下次，其餘都指定併入一份由 penholder 主筆的 baseline。
2. **TR 內文凍結是程序造成的，不是沒人關心。** SA2#170–#172 一共收到 **59 件 solution 更新提案，全部 Not Handled**。被提更新最多的是 #16（6 件）、#6（5 件），而且多數出自非原提案方。
3. **用公司數來算，AMF 之爭的熱度和本站先前用 solution 數算的方向相反。** 先前用「同立場 solution 數」得出經 AMF（6）多於直連（4）。改用 SA2#173 實際表態的公司數：最終修正案 S2-2601651 由 13 家連署，舉手表決「只走直連」支持 19、反對 3；經 AMF 的 baseline 只有 5 家提案方，另有 CEWiT 主張兩案並列（Tejas 同時出現在經 AMF 和兩案並列兩份文件上）。**更正：直連這方的支持遠多於經 AMF 那方，結果並不意外。**
4. **最具辨識力的熱度訊號有四種：** penholder 歸屬、進場前的合併與改連署、第三方更新嘗試、SA2#173 的陣營分裂。結論文件的連署幾乎全員參與（12～25 家），單看連署數分不出強弱。

---

## 1. 方法

1. 從 6 份 TdocsByAgenda 擷取所有含 FS_Sensing_ARC 的列，欄位包括：會議、議程、tdoc、類型、標題、提案方、說明、決定。
2. 依說明欄的「Revision of」「Revised … to」「Merge into／Merged into」把 tdoc 串成家族（union-find）。一個家族＝原始提案＋各修訂版＋被併入的文件。
3. 把 SA2#169、#170 核准的新方案 tdoc 對應到 TR v0.2.0、v0.3.0 的 Sol #1–#39。依據是標題相似度、TR 中 solution 的排列順序，以及後續「Update of solution #n」的提案方是否一致（例如 Sony 更新 #15、CEWiT 更新 #17、ETRI 以 "Solution 6.4" 更新 #4）。
   - 信心度中等的只有 **#16 ↔ Lenovo S2-2505881**。#16 的更新嘗試都來自他人（ZTE、Huawei、NTT DOCOMO），沒有原提案方自己的更新可以佐證。
4. 「更新嘗試」= SA2#170–#173 標題含「Sol/Solution #n」或「Solution 6.n Update」的 P-CR。SA2#170 有 3 份 Toyota 的 #38 新方案文件標題含 "Update"，已排除。標題寫「Solution 6.n」的只算到 #n，一份文件只算一次。三次會議的件數（16／31／12）和主席筆記 "Solutions updates" 標題下的 Docs:= 相同。
5. §3.3、§3.4 的分組與件數以主席筆記的議題標題為準（例如 "Solutions for KI#2 authorization/revocation"、"Conclusion for KI#5"）。只計首次提交，包含前次會議未處理、這次重新提交的文件，不含會內修訂版與撤回件。主席筆記共列有 10 份 TdocsByAgenda 沒有的文件，類型都是 DISCUSSION 或 LS。其中 Tejas 的 3 份（S2-2505039、S2-2505040、S2-2505623）實際是新方案及其修訂版，已補入 §2 和 §3.3；其餘 7 份是討論文件或 LS，不影響本報告的計數。

## 2. 39 solutions 與 tdoc 對照（含熱度指標）

欄位說明：
- 連署 = 核准 tdoc 的公司數（Huawei/HiSilicon、Nokia/NSB 各算一家）
- 修訂 = 進場前的修訂次數
- 更新 = SA2#170–#172 的更新嘗試數，全部 Not Handled
- 第三方 = 提更新的非原提案方

| # | 核准 tdoc | 提案方（連署） | 連署 | 修訂 | 更新 | 第三方 |
|---|---|---|---|---|---|---|
| 1 | S2-2506061 | Qualcomm、Deutsche Telekom | 2 | 3 | 0 | — |
| 2 | S2-2506062 | LG Electronics、OPPO | 2 | 3 | 1 | — |
| 3 | S2-2506063 | Huawei、CAICT、China Mobile、ZTE、CATT、Deutsche Telekom、OPPO、China Telecom、KDDI、Rakuten Mobile | **10** | 3 | 3 | KPN、Toyota、Xiaomi |
| 4 | S2-2505811 | ETRI | 1 | 2 | 3 | — |
| 5 | S2-2506064 | NTT DOCOMO、Nokia | 2 | 3 | 2 | — |
| 6 | S2-2505814 | InterDigital | 1 | 2 | **5** | KPN、Lenovo、NTT DOCOMO、TNO |
| 7 | S2-2506065 | Intel、NTT DOCOMO | 2 | 3 | 0 | — |
| 8 | S2-2506066 | China Mobile、Nokia、Lenovo、KDDI | 4 | 3 | 3 | — |
| 9 | S2-2505874 | Samsung | 1 | 2 | 1 | — |
| 10 | S2-2505876 | Toyota、BUPT | 2 | 3 | 0 | — |
| 11 | S2-2505875（＋S2-2507810） | Xiaomi | 1 | 3 | 2 | Futurewei |
| 12 | S2-2505877 | Tejas | 1 | 2※ | 2 | — |
| 13 | S2-2505878 | vivo | 1 | 2 | 3 | — |
| 14 | S2-2505879 | Futurewei | 1 | 2 | 0 | — |
| 15 | S2-2506102 | Sony | 1 | 3 | 4 | China Mobile |
| 16 | S2-2505881 | Lenovo（中信心） | 1 | 2 | **6** | Huawei、NTT DOCOMO、ZTE |
| 17 | S2-2505882 | CEWiT | 1 | 2 | 1 | — |
| 18 | S2-2505883 | OPPO | 1 | 2 | 2 | — |
| 19 | S2-2506060 | Apple | 1 | 2 | 0 | — |
| 20 | S2-2505884 | China Mobile | 1 | 2 | 4 | Huawei |
| 21 | S2-2507773 | CATT | 1 | 2 | 1 | — |
| 22 | S2-2507774 | vivo、ETRI | 2 | 2 | 2 | — |
| 23 | S2-2507813 | Apple | 1 | 3 | 2 | Mitsubishi Electric |
| 24 | S2-2507814 | Intel | 1 | 3 | 4 | KPN、TNO |
| 25 | S2-2507815 | BUPT、Toyota | 2 | 3 | 1 | — |
| 26 | S2-2507778 | China Telecom、Toyota | 2 | 2 | 0 | — |
| 27 | S2-2507779 | Nokia、KDDI | 2 | 2 | 0 | — |
| 28 | S2-2507816 | Ericsson | 1 | 3 | 1 | — |
| 29 | S2-2507817 | China Mobile | 1 | 3 | 0 | — |
| 30 | S2-2507782 | ETRI | 1 | 2 | 0 | — |
| 31 | S2-2507820 | OPPO | 1 | 3 | 1 | Toyota |
| 32 | S2-2507818 | CEWiT、KPN | 2 | 3 | 0 | — |
| 33 | S2-2507819 | InterDigital | 1 | 3 | 0 | — |
| 34 | S2-2507805 | ZTE | 1 | 3 | 1 | — |
| 35 | S2-2507806 | Samsung | 1 | 2 | 1 | — |
| 36 | S2-2507807 | Lenovo、Futurewei、China Telecom、Toyota | 4 | 2 | 1 | Ericsson |
| 37 | S2-2507808 | Huawei、CAICT | 2 | 2 | 1 | Ericsson |
| 38 | S2-2507809 | Toyota、BUPT | 2 | 2 | 1 | — |
| 39 | S2-2507811 | Tejas | 1 | 2 | 0 | — |

※ #12 的修訂次數依主席筆記：S2-2505040 → S2-2505623 → S2-2505877。前兩版 TdocsByAgenda 沒有列出。

## 3. 演進：哪些併入了哪個

### 3.1 進場前的正式合併（tdoc 說明欄明載）

| 被併入的 | 併入對象 | 依據 |
|---|---|---|
| Rakuten Mobile、NIST 的 KI#1 架構方案 S2-2504609 → S2-2505577 | Huawei 等的 #3（S2-2505579 → S2-2506063） | S2-2505577："Merged into S2-2505579"；Rakuten Mobile 列入 #3 連署 |
| ETRI 的「NRPPa Extension over Direct Connection」S2-2507089 | vivo 的 #22（S2-2506609 → S2-2507774） | S2-2507089："Merge into S2-2506609"；ETRI 列入 #22 連署 |
| Xiaomi 的「Revocation of an ongoing Sensing Service」S2-2507810（另案核准） | 既有 Sol #11 | 核准後沒有新增 solution 編號；TR v0.3.0 的 Sol #11 新增 §6.11.2.3，標題相同。**這一條是編輯合併，屬推論** |

### 3.2 進場前的改連署（推論，依據是同一會議的未處理紀錄與連署名單）

SA2#169 主席筆記 "Solutions for KI#1 architectural" 組有 10 份新方案 Not Handled：OPPO S2-2504601、vivo S2-2504821、China Telecom S2-2504839、ZTE S2-2504950、Lenovo＋China Telecom S2-2505135、Samsung S2-2505215、CATT S2-2505397、Xiaomi S2-2505414、Nokia S2-2505431、Tejas S2-2505039（只列在主席筆記）。其中 OPPO、China Telecom、ZTE、CATT 四家的名字出現在 #3 的連署名單上，看起來是轉去支持 #3。但 OPPO、ZTE 在 SA2#170 又提了 KI#1 架構方案（OPPO 重提為 S2-2506285，ZTE 另提 S2-2506766），都沒被處理；對這兩家來說，連署 #3 不等於放棄自己的方案。vivo、Lenovo、Samsung、Xiaomi、Nokia、Tejas 沒有連署 #3：Lenovo、Nokia 改去連署 #8，Tejas 的 KI#2 方案另成 #12。這也解釋了為什麼 #3 的 SCF/SPF 用語最後成為 §8.1 P1 的骨架。

### 3.3 進場時的競爭（新方案首次提交，不含修訂版）

| KI | SA2#169 有處理 | SA2#169 未處理 | SA2#170 有處理 | SA2#170 未處理 |
|---|---|---|---|---|
| KI#1 架構 | 8 | 10 | 1 | 6 |
| KI#2 授權 | 5 | 9 | 4 | 3 |
| KI#3 發現／選擇 | 5 | 10 | 2 | 3 |
| KI#4 資料傳輸 | 1 | 7 | 6 | 7 |
| KI#5 曝露 | 1 | 11 | 7 | 3 |
| KI#6 參數配置 | 1 | 1 | 2 | 1 |
| 合計 | 21 | 48 | 22 | 23 |

計數規則：
- 分組依主席筆記的議題標題，例如 #169 的 "Solutions for KI#1 architectural"、#170 的 "New Solutions for KI#4 Sensing data collection"。標題寫了多個 KI 或沒寫 KI 的提案，也照筆記歸組；例如 Tejas 的 S2-2506708（後來的 #39）在 #170 列於 KI#3 組。
- 各組件數和筆記標示的 Docs:= 相同，只有一處例外：#169 KI#2 組的 OPPO S2-2504602 標題是 "Key issue for WT#2"，不是新方案，表中不計。
- 處理結果取 TdocsByAgenda 的決定欄。「有處理」包含修訂、核准、併入、Noted。ETRI 的 S2-2507089 決定欄是 Not Handled，說明欄寫 Merge into S2-2506609（見 §3.1），表中按決定欄算作未處理。
- 核對 #169：有處理的 21 份中，Rakuten／NIST 併入 #3，其餘 20 份成為 #1–#20。
- 核對 #170：有處理的 22 份中，2 份 Noted，Xiaomi 的 S2-2507436 寫入既有 #11，其餘 19 份成為 #21–#39。
- SA2#171 另有 2 份新方案重提（vivo 的 KI#2 方案、Samsung 的 KI#4 方案），都沒被處理。此後再沒有新方案。

讀法：
- **曝露類（KI#5）幾乎全在第二批進場。** SA2#169 的 KI#5 有 12 份提案，只處理了 Apple 一份（後來的 #19）。未處理的 11 份裡，有 6 份在 SA2#170 重新提交後才被處理：Ericsson、Nokia、OPPO、China Mobile、CEWiT、ETRI。這 6 份加上 InterDigital 的新提案，成為 #27–#33。
- **資料直連路線（KI#4）在第二批才成形。** SA2#169 只處理 1 份（OPPO，後來的 #18）。SA2#170 處理了 6 份，成為 #21–#26，直連的 #21、#22、#25 都在這一批。

### 3.4 進場後：solution 凍結，戰場移到結論提案

| 會議 | solution 更新提案 | 處理結果 |
|---|---|---|
| SA2#170 | 16 | 全部 Not Handled |
| SA2#171 | 31 | 全部 Not Handled |
| SA2#172 | 12 | 全部 Not Handled |
| 合計 | 59 | |

同一時期的結論類提案（含暫定協議、結論、解決 EN；首次提交件數）：

| 會議 | KI#1 | KI#2 | KI#3 | KI#4 | KI#5 | KI#6 |
|---|---|---|---|---|---|---|
| SA2#171 | 15 | 11 | 11 | 17 | 11 | 7 |
| SA2#172 | 19 | 13 | 16 | 17 | 13 | 16 |
| SA2#173 | 14 | — | — | — | — | — |

（#171、#172 取主席筆記各 KI 標題下的 Docs:=。#173 的筆記沒有分 KI 標題，14 是當次 P-CR 的首次提交數，全部針對 KI#1。）

除了 #171 的 KI#5、KI#6，每個 KI 都是「一份 baseline＋其他提案指定併入」：#171 的決定欄寫 Merged；#172 的說明欄寫 Merge into，決定欄為 Not Handled。penholder 和最終連署家數如下：

| 會議 | KI | 核准 tdoc | penholder | 連署家數 |
|---|---|---|---|---|
| #171 | KI#1 暫定 | S2-2509659 | Xiaomi（rapporteur） | 21 |
| #171 | KI#2 暫定 | S2-2509824 | Huawei | 22 |
| #171 | KI#3 暫定 | S2-2509825 | Qualcomm | 24+ |
| #171 | KI#4 暫定 | S2-2509826 | Ericsson | 16 |
| #171 | KI#5、KI#6 | — | 全部 Not Handled，延到 #172 | — |
| #172 | KI#1 結論 | S2-2511301 | Xiaomi | 12+ |
| #172 | KI#2 結論 | S2-2511042 | vivo | 18 |
| #172 | KI#3 結論 | S2-2511040 | LG Electronics | 25 |
| #172 | KI#4 結論 | S2-2511044 | ZTE | 17 |
| #172 | KI#5 結論 | S2-2511049 | Nokia | 23 |
| #172 | KI#6 結論 | S2-2511041 | Samsung | 19 |
| #173 | KI#1 修正（P4a） | S2-2601651 | OPPO | 13 |

（連署家數＝去重後的公司數，Huawei／HiSilicon、Nokia／NSB、CMCC／China Mobile 各算一家。「+」表示 TdocsByAgenda 的提案方欄位被截斷，實際至少這麼多家。#173 的 13 家取自 S2-2601651 原文，TdocsByAgenda 只列 9 個名稱。）

## 4. 真熱度：四種有辨識力的訊號

### 4.1 進場時的聚集度

#3 有 10 家連署（其中 4 家自己的架構方案沒被處理，1 家是併入），是 39 個裡唯一形成聯盟的 solution。其次是 #8（China Mobile、Nokia、Lenovo、KDDI）和 #36（Lenovo、Futurewei、China Telecom、Toyota），各 4 家。其餘 36 個是 1～2 家的單獨或雙家提案。

### 4.2 第三方更新嘗試（別人想改你的方案）

- **#16（SE 向 SF 註冊，Lenovo）**：6 件，全部來自第三方（Huawei、NTT DOCOMO、ZTE 各 2 件），主題是 SE 選擇準則。
- **#6（依服務區的 Sensing NF，InterDigital）**：5 件，其中 2 件是 InterDigital 自己提的；另 3 件來自 4 家第三方（Lenovo；KPN、TNO；KPN、TNO、NTT DOCOMO）。標題寫明主題的 2 件（KPN、TNO）都是 SE 選擇。
- **#3**：Toyota、KPN、Xiaomi 想改 SCF/SPF 切分的細節。

這三個集中在「SF 怎麼選 gNB、SE 資訊從哪來」，正好是 §8.3 NOTE 1、NOTE 2 留成 FFS 的地方。熱度高但沒有收斂，是一個值得在 Rel-20 規範階段持續追蹤的爭點（推論）。

### 4.3 Penholder 歸屬

主筆者可以決定 baseline 的文字。KI#1 由 rapporteur Xiaomi 從頭主筆到 #172，#173 改由 OPPO 主筆。KI#2 由 Huawei 換成 vivo，KI#3 由 Qualcomm 換成 LG，KI#4 由 Ericsson 換成 ZTE。KI#5、KI#6 在 #171 完全沒處理，到 #172 才由 Nokia、Samsung 主筆。

### 4.4 SA2#173 的 AMF 之爭（公司層）

| 立場 | 文件 | 提案方 | 結果 |
|---|---|---|---|
| 直連（baseline） | S2-2600580 | Qualcomm | Postponed（時間不足） |
| 直連 | S2-2600783 | Ericsson、AT&T | Not Handled |
| 直連（最終採用） | S2-2601651（S2-2601707 r04，email 核准） | OPPO、Huawei/HiSilicon、Xiaomi、LGE、China Mobile、AT&T、ZTE、Apple | **Approved** |
| 經 AMF（baseline） | S2-2600620（另有討論文件 S2-2600619） | Nokia、NTT DOCOMO、Samsung、KPN、Tejas | Not Handled |
| 兩案並列（baseline） | S2-2600983 | CEWiT、Tejas | Not Handled |

- **公司數**：直連 13 家（S2-2601651 最終連署：OPPO、Huawei、Xiaomi、LGE、China Mobile、AT&T、ZTE、Apple、vivo、Ericsson、Qualcomm、CATT、China Telecom），經 AMF 5 家，兩案並列 2 家（Tejas 兩邊都有）。舉手表決「只走直連」為支持 19、不支持 6、反對 3。
- **和 solution 的對應**：經 AMF 陣營正好是落敗 solution 的提案方：#5（NTT DOCOMO、Nokia）、#39 與 #12（Tejas）、#35（Samsung）、#7（共同提案方 NTT DOCOMO）。直連陣營則包括 #1 的提案方 Qualcomm，以及 #37 的提案方 Huawei。
- **程序面**：兩個 baseline 都沒被處理，最後由 OPPO 的修正文件經 email 核准定案。所以 P4a 不是「直連 baseline 勝出」，而是另一份多方連署的修正案勝出。實際的決定機制是一次舉手表決（show of hands）之後宣告的 Working Agreement，見 §6。
- **補充（主席筆記）**：email 討論中，vivo、Ericsson、Qualcomm、CATT 也陸續要求連署，r04 加入 5 家連署（內容不變）。TdocsByAgenda 只列 9 個名稱（Huawei 與 HiSilicon 合算，共 8 家），沒有反映 r04 的增列。S2-2601651 原文的提案方共 14 個名稱（Huawei 與 HiSilicon 算一家，共 13 家），已核對原文。舉手表決的票數見 [爭點技術路線分析](dispute-analysis.md) §1。

## 5. 限制與下一步

1. **決定理由**：已補讀六次會議的主席筆記，見 §6。主席筆記多半只記「怎麼改、怎麼決定」，很少記「為什麼」。逐家論點要看各 tdoc 原文或 email 討論串。
2. **連署＝表態，不等於擁有專利。** 但「採納機制的原提案方」可以作為之後 Rel-20 TS 出來時，比對 SEP 宣告的候選清單。這只是推論。
3. **#16 的對應信心中等**，需要打開 S2-2505881 原文確認。各 tdoc 原文 zip 都在 FTP 的 Docs/ 下，也還沒下載。
4. 版本溯源報告 §1 第 4 點用 solution 數得出「經 AMF 6 > 直連 4」，依本報告 §4.4 公司層數據應更正，已在該報告加註。

---

## 6. 主席筆記補充：每次會議的決定與理由

- 來源：SA2#168–#173 主席筆記，FS_Sensing_ARC 議程 20.2.1。#168 只有分場筆記，#169–#173 用會末 Combined 版；另加 #172、#173 的 email 核准清單。
- 位置：3GPP 官方 FTP 各會議資料夾的 INBOX/Chair_Notes/。
- 引文為筆記原文；「推論」另外標明。

### SA2#168（2025-04）：誰寫了 KI 的骨架

- 各議題選定的 baseline：
  - 術語：Huawei（S2-2503798）
  - 架構假設：China Telecom（S2-2503272）
  - 架構需求：Ericsson（S2-2502960）
  - KI#1：Apple（S2-2503079）
  - KI#2：Qualcomm（S2-2503820，筆記寫 "use as baseline?"）
  - KI#3：vivo（S2-2503063）
  - KI#4：OPPO（S2-2502942）
  - KI#5：China Mobile（S2-2503423）
  - KI#6：Sony（S2-2503146）
- 有 11 份架構假設／需求提案被拆開，分別併入上面兩份 baseline。提案方包括 LG、vivo、OPPO、Ofinno、Google、InterDigital、China Mobile、ZTE、Nokia、Huawei、Qualcomm。

### SA2#169（2025-05）：第一批 20 個 solution，主席當場改了什麼

| 對象 | 主席筆記記載的修改 | 意義 |
|---|---|---|
| #1 Qualcomm | "Remove the annex"／"Replace all the SBI to new interface" | 直連一開始就被定位成「非 SBI 的新介面」 |
| #3 Huawei 等 | NOTE 改為 EN，並寫入 SCF 與 SPF 的定義 | 這組定義後來成為 §8.1 P1 |
| #5 NTT DOCOMO | 加 EN："The new service details are FFS"（TR ¶721） | AMF 新服務的細節從一開始就未定 |
| #7 Intel | 刪除 "with possible analytics functions (e.g. NWDAF/ADRF) for processing or storing sensing data" | 用分析類 NF 做儲存的路線在進場時就被拿掉（推論：P2 的前兆） |
| #8 China Mobile | 加 EN：服務取消時，SE 授權是否一併撤銷 FFS | — |
| #17 CEWiT | 加 EN：SE 怎麼把能力提供給 AMF、存在哪裡 FFS | 經 AMF 發現 SE 的弱點從第一天就被標出 |
| AT&T S2-2505808 | 同意 "caching and/or storage and/or retrieval of sensing data" 的需求 | 需求保留了，但 #171 決定不設專用儲存 NF |

- **v0.2.0 的 Editor's note 已經限縮範圍**：Q2 的工作只做共通部分，不碰 RAN 或 UE 專屬的感知模式；"Any UE/RAN aspects will be aligned with TSG RAN after TSGs#108"（v0.2.0 §1 Editor's note）。

### SA2#170（2025-08）：範圍收斂到 gNB，這是 UE 方案出局的真正原因

- Apple、Xiaomi 的 S2-2507769「TR and SID scope alignment」被核准（合併了 S2-2506765）。TR v0.3.0 的 Scope 從此改為 "In this study, the scope is restricted to gNB-based sensing"，並加註 "The scope is aligned to the Rel-20 5G-A RAN ISAC study scope"。
- 同一場，Transsion 的 UE 識別方案（S2-2506314）被 Noted，主席註記 "only gNB part, remove UE part"。
- **結論**：#7（UE 部分）、#18（UE 作 SE）、#19（UE 作 SE 或消費者）這些「讓 UE 參與」的設計，不是在 SA2 技術討論中被駁回，而是在 TSG#108 之後跟著 RAN 的 Rel-20 研究範圍被切掉。UE 作消費者（#2、#33）則到 #172 才由 §8.5 NOTE 4 收掉。
- Ericsson 的「Direct Sensing Association between gNB and SnCF」（S2-2506344）、ZTE、Nokia 的資料傳輸方案都排在第二輪，最後 Not Handled。
- Huawei 想先做 KI#1–3 的暫定結論（S2-2506694，"Only KI#123 part"），沒被處理。

### SA2#171（2025-10）：暫定協議

- KI#1 暫定協議 S2-2509659 照筆記原文同意：P1 單一 SF（可內含 SCF／SPF，兩者之間無標準介面）、P2 不設專用儲存 NF、P3 只有 gNB 是 SE。
- KI#4 暫定協議 S2-2509826 "Remove 1st bullet"。被刪的條文內容要看 tdoc 原文。
- KI#5、KI#6 全部 Not Handled，延到 #172。
- OPPO 起草了給 RAN3 的資料收集 LS（S2-2508282 → S2-2509417）。CATT 提議增加 Sensing QoS 術語，主席註記 "To capture all the potential new terms during the discussion of interim agreements"。

### SA2#172（2025-11）：結論，以及 AMF 問題如何被掛起

- **KI#1 結論 S2-2511301**：主席註記 "Remove text in yellow, add Editor's Note: Whether Sensing control signalling is exchanged between SE and SF directly without AMF involvement, or with AMF involvement, is FFS and will be resolved in the next meeting"。有爭議的黃色段落被整段拿掉，只留 EN。
- **KI#6 結論 S2-2511041**：刪掉 "Sensing function will send either directly the sensing parameters to sensing entity for the sensing service or via AMF in a container"，以及 "The sensing parameters by SF to gNB directly or via AMF will be aligned with KI#1 conclusions" 這條 NOTE。參數走哪條路，被一併推給 KI#1 去決定。
- **TR 封面**（S2-2511056）：完成度記為 93%，未決事項只寫這一條 AMF EN。
- **給 RAN3 的 LS**（S2-2511045）同意送出，請 RAN3 在自己的研究中考慮 TR 第 8 章的結論。

### SA2#173（2026-02）：舉手表決與 Working Agreement

- 主席安排三份 baseline 平行處理：
  - 直連：Qualcomm S2-2600580
  - 經 AMF：Nokia、NTT DOCOMO、Samsung、KPN、Tejas 的 S2-2600620，另附討論文件 S2-2600619
  - 兩案並列：CEWiT、Tejas 的 S2-2600983
- **決定方式**：S2-2601706「Draft SoH for the open issue in KI#1」（Xiaomi、Apple）。主席筆記原文："Way forward: A Working Agreement is declared for moving forward with only Option A, and the Sensing WID KI#1 will based on this way forward"。
  - **Option A 即直連**：舉手表決投影片 S2-2601706 寫明 Option A 是 "Sensing control signalling is exchanged via direct connection between SE and SF without AMF"，票數見[爭點技術路線分析](dispute-analysis.md)§1。email 討論中，Xiaomi 也要求刪掉提出「both options」的討論段落，理由是它 "not reflecting the Working Agreement"。
- **落實方式**：OPPO 的 S2-2601707 送 email 核准。
  - r01–r03：依 Working Agreement 刪掉討論段落。屬經 AMF 陣營的 Samsung 也同意刪。
  - vivo、Ericsson、Qualcomm、CATT 陸續要求連署；r04 增列 5 家，內容不變。
  - 最後以 S2-2601651 核准，成為 v2.1.0。
- **封面**（S2-2601108 → S2-2601653）：Huawei 要求封面寫明「結論是依據 Working Agreement 做成的，Working Agreement 確認後即視為 100% 完成」。Ericsson 提議把 S2-2601707 一併放進 email 核准，獲 OPPO、vivo、LGE、Huawei、Apple、Qualcomm 支持。
- **給 RAN3 的 LS**：Ericsson 起草的「LS on Sensing control signalling between the Sensing Function and Sensing Entities」（S2-2601708）在會末仍是 OPEN。

### 小結：各類方案出局的直接原因

| 出局的設計 | 直接原因 | 時點 |
|---|---|---|
| UE 作感知實體（#7 的 UE 部分、#18、#19） | TSG 層級把研究範圍與 RAN Rel-20 ISAC 研究對齊，只剩 gNB | SA2#170（v0.3.0 Scope） |
| UE 作消費者（#2、#33） | §8.5 NOTE 4 假設請求方＝消費者＝AF | SA2#172 |
| 分析／儲存類 NF（#7 的 NWDAF/ADRF、#12、#26、#31、#38） | #169 主席刪除 NWDAF/ADRF 儲存描述；#171 P2 不設專用儲存 NF | SA2#169 → #171 |
| 多個獨立 NF、閘道型 NF（#9、#10、#19、#24、#34） | #171 P1 單一 SF；#172 P5 一個請求只選一個 SF | SA2#171 → #172 |
| 控制信令經 AMF（#5、#39、#35b；#13、#17 的 AMF 發現） | #172 掛起成 EN；#173 舉手表決後宣告只走 Option A | SA2#172 → #173 |

---

## 7. 更正紀錄（2026-10-27）

製作內部簡報包時重新核對了一次，之後再用主席筆記的分組標題與 Docs:= 做第二種算法交叉檢查。更正如下：

| 位置 | 原內容 | 更正後 | 原因 |
|---|---|---|---|
| §0、§2、§4.2：#6 的更新件數 | 8 件，5 家第三方（含 ETRI） | 5 件，4 家第三方 | ETRI 的 "Solution 6.4" 是更新 #4，原算法把它重複算進 #6 |
| §2：#21 的更新件數 | 2 | 1 | 同一份文件算了兩次 |
| §2：#12 的修訂次數 | 0 | 2 | 前兩版只列在主席筆記 |
| §0、§3.4：solution 更新提案 | 58（#171 為 30） | 59（#171 為 31） | 按文件去重後重算，與主席筆記 "Solutions updates" 的 Docs:= 一致 |
| §3.3：各 KI 新方案處理表 | 未處理 38／12，有處理 18／14 | 未處理 48／23，有處理 21／22 | 原算法漏算三類：重新提交的提案、標題沒寫 solution 的提案、只列在主席筆記的 Tejas 文件。分組改依主席筆記 |
| §3.2：未處理的架構方案 | 9 份 | 10 份 | 補上 Tejas S2-2505039 |
| §0、§3.2：連署 #3 的解讀 | 「等於放棄自己的方案」 | OPPO、ZTE 在 #170 仍提出自己的 KI#1 架構方案 | 補算重新提交的提案後發現 |
| §0、§3.4：結論類提案件數 | 6～21 份（例：#171 KI#4 為 21） | 7～19 份（例：#171 KI#4 為 17） | 原表把會內修訂版也算進去，改用主席筆記的 Docs:= |
| §3.4：penholder 文件的連署家數 | 24、25、17、12、19、24、21、9 | 22、24+、16、12+、18、23、19、13 | 改為去重後的公司數；「+」表示提案方欄位被截斷；#173 依 S2-2601651 原文 |
| §4.4：TdocsByAgenda 的列名 | 9 家 | 9 個名稱（8 家） | Huawei 與 HiSilicon 合算一家 |
