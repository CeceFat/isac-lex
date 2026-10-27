# TR 23.700-14 爭點技術路線分析

- 日期：2026-10-27
- 補強對象：前三份報告（版本溯源、tdoc 層熱度、演進圖）只畫出了各方的消長，沒有拆解每個爭點的技術差異。本報告逐一拆解七個爭點。
- 證據來源：
  - TR 23.700-14 v20.0.0 的 39 個 solution 原文，以 Sol #n 與小節標示
  - SA2#173 各陣營的立場文件（3GPP 官方 FTP，TSGS2_173_Goa_2026-02/Docs/）：S2-2600580、S2-2600619、S2-2600620、S2-2600982、S2-2600983、S2-2600783、S2-2600111、S2-2601706（舉手表決投影片）、S2-2601708、S2-2601651
  - 主席筆記
- 標示規則：引號內為原文；「分析」「推論」是本報告的判斷。

---

## 0. 結論先講

1. **Option A 已確認是直連。** 舉手表決投影片 S2-2601706 的 Proposal-1 是「only option A (not B)」，內容原文為 "Sensing control signalling is exchanged via direct connection between SE and SF without AMF"。三輪票數：支持 14 → 18 → 19，不支持 8 → 6 → 6，反對 3 家（Samsung、Nokia、CEWiT）。只走經 AMF 的 Proposal-2 最後只有 8 票支持、8 家反對。
2. **七個爭點的技術核心，都是「新功能要不要寄生在既有節點上」。** 每一題都可以讀成同一組取捨：
   - 寄生既有節點（AMF、NWDAF/DCCF、UDR、NEF）：重用現有安全與營運框架，但會增加既有節點的負擔與規格修改。
   - 另立新路徑（SF 直連、SF 內含處理、SF 自持資料）：規格乾淨、不干擾通訊業務，但要新建介面，並重做安全、發現、維運。
   Rel-20 的結論在每一題都選了後者。
3. **AMF 之爭真正的技術分歧點**有四個：N2 有沒有通用的「非 UE 關聯」傳輸程序、AMF 處理負擔、SF 端要維護多少連線、未來 UE 加入時是否需要單一路徑。協定堆疊不是分歧點：雙方都承認 RAN3 已同意控制面沿用 SCTP（S2-2600580 引 R3-258820；S2-2600619 引 RAN3#130）。
4. **UE 當感知實體很可能會回來，最可能的時點是 6G。** 一旦回來，落敗的 AMF 路線會跟著翻案，因為連到 UE 的控制路徑只能經 AMF（NAS）。落敗陣營在 #173 的文件裡已經明白預留了這個論點（見 §8）。

---

## 1. Option 狀態確認（S2-2601706）

| 提案 | 內容 | baseline | 支持 | 不支持 | 反對 |
|---|---|---|---|---|---|
| Proposal-1 | 只走 Option A（直連，不經 AMF） | S2-2600580（Qualcomm） | 14 → 18 → 19 | 8 → 6 → 6 | 3 → 3 → 3（Samsung、Nokia、CEWiT） |
| Proposal-2 | 只走 Option B（經 AMF） | S2-2600620（Nokia 等） | 6 → 6 → 8 | 9 → 12 → 15 | 6 → 6 → 8 |
| Proposal-3a | A、B 擇一並存（不可同時部署） | S2-2600983（CEWiT、Tejas） | 3 → 7 | 4 → 11 | 1 → 8 |
| Proposal-3b | A 必備、B 選配（不可同時部署） | S2-2600947（OPPO 原始版） | 9 → 14 → 10 | 7 → 7 → 12 | 1 → 4 → 10 |

- 結果原文："Way forward: A Working Agreement is declared for moving forward with only Option A, and the Sensing WID KI#1 will based on this way forward"。
- **一個轉折**：OPPO 的原始文件 S2-2600947 是折衷案 3b（A 必備、B 選配）。3b 在第二輪拿到 14 票，但反對數也從 1 家升到 10 家。宣告 Working Agreement 之後，OPPO 的修正案（S2-2601707 → S2-2601651）把 B 選配拿掉，只留 A。Xiaomi 在 email 討論中要求刪掉提出「both options」的討論段落，理由是它 "not reflecting the Working Agreement"（#173 email 核准清單）。
- **最終連署**：S2-2601651 原文列 14 個名稱（Huawei 與 HiSilicon 算一家，共 13 家）：OPPO、Huawei、HiSilicon、Xiaomi、LGE、China Mobile、AT&T、ZTE、Apple、vivo、Ericsson、Qualcomm、CATT、China Telecom。這修正了先前 tdoc 清單只列 9 家的資料。
- **對 RAN3 的告知**：S2-2601708 草稿寫明 "SA2 has declared the working agreement and Architecure#1 will be adopted as the way forward"（會末仍是 OPEN）。

---

## 2. 爭點一：控制信令路徑（SF ↔ gNB 是否經 AMF）

### 2.1 三種架構的術語

Ericsson 在 S2-2600783 §1.1 把架構分成三種：
- **indirect**：控制和資料都經 AMF，代表是 Sol #5。#172 決定資料直連後，這一型已出局。
- **hybrid**：資料直連，控制經 AMF，即 #173 的 Option B。
- **direct**：兩者都直連，即 Option A。

### 2.2 逐點論據對照

| 技術面向 | 直連方（Option A） | 經 AMF 方（Option B） | 分析 |
|---|---|---|---|
| **N2 能不能直接承載** | Qualcomm：N2 是點對點介面，每個 elementary procedure 都要個別定義；TS 38.413 沒有通用的非 UE 關聯傳輸程序，"They cannot be reused for sensing signalling"，所以一定要新增 NGAP 程序（S2-2600580 §1） | Nokia 等："AMF is the designated control-plane gateway"，gNB "is designed to accept configuration/control messages only through the AMF"（S2-2600619 §1.2） | **關鍵分歧。** 經 AMF 方主張的是架構原則，直連方舉的是規格事實：現有 NGAP 確實沒有可以直接重用的通用容器。所以兩條路都要新增程序，經 AMF 並不省規格工作。這也是 Option B 在投票中流失的主因（推論） |
| **協定堆疊** | RAN3 已同意 NxAP 跑在 SCTP 上，gNB 端的 SCTP 以下可以重用；直連的好處是 NxAP 設計不必顧及和 NGAP 的向後相容（S2-2600580） | "The Control Plane stack in 5G is SCTP-based and it continues to be the same for Sensing too"（S2-2600619，RAN3#130） | 雙方對協定堆疊沒有爭議。差別只在終點：SF 還是 AMF |
| **AMF 負擔** | AMF 要處理每一則感知訊息，還要做 Namf 服務與 N2 程序之間的轉換，"could burden the most important node of the 5GC"（S2-2600580） | AMF 的集中中介 "is designed to handle scale efficiently"（S2-2600619） | 取捨：負擔放在 AMF，還是放在 SF |
| **SF 端連線規模** | SF 本來就要和 gNB 直連傳資料，控制直連可以共用發現與連線建立（S2-2600580） | SF 要維護對每台 gNB 的直連，"SF becomes a bottleneck"；多個 SF 時更複雜（S2-2600619；CEWiT S2-2600982 §1.2.4） | **未完全解決。** 資料直連已定案，SF–gNB 連線本來就存在，所以這一點的邊際差異縮小了。但 SF 數量 × gNB 數量的維護成本，會變成規範階段的議題 |
| **發現與 gNB 狀態** | SF 不管怎樣都得先決定目標 gNB，AMF "does not provide any assistance"（S2-2600580） | AMF 知道 gNB 的連線狀態與能力，可以取代 SF 端的預先設定（S2-2600982 §1.2.3） | 這和 §8.3 NOTE 1（SE 資訊經 OAM 或信令取得仍 FFS）直接相關，見爭點四 |
| **安全** | 直連可以把感知服務和通訊服務隔離，"improves security and scalability"（S2-2600783 Obs.5） | 若直連，"there would be need for additional work to ensure secure transmission"；AMF 是可信的閘道（S2-2600619） | 都交給 SA3（§8.1 NOTE 5）。雙方說的都是方向，沒有具體威脅模型 |
| **生態系** | 兩案並存 "leads to ecosystem fragmentation"，在 MOCN 等多業者場景有互通問題（S2-2600783 §1.3） | 兩案並存 "provide flexibility to the operator"（S2-2600982） | 投票結果反映多數人站在「單一選項」這邊 |
| **前瞻性** | "there is no UE involvement in 5GA sensing in this release"（S2-2600580）；中國移動：AMF 主要服務 UE，"the introduction of the AMF is not mandatory"（S2-2600111） | "UEs may be in the scope of future releases"；舊版 gNB 在未來雙站／多站場景當發射端時，直連要求會成為障礙（S2-2600619） | 見 §8：這是落敗方為未來保留的論點 |
| **時程** | 中國移動：加入 AMF 需要另外排 TU 討論 AMF 選擇、AMF–SCF 介面等，TU 有限（S2-2600111） | 既有 N2 經過時間驗證，可以 "quickly adopt the new service"（S2-2600982） | 雙方都用「快」當理由。直連方說的是規格時程快，經 AMF 方說的是部署穩定快 |

### 2.3 立場與原 solution 的對應

| 陣營 | 對應的 solution |
|---|---|
| 直連 | #1（Qualcomm）；#26 的 SCF–gNB 新介面；#34（直連）；#35 a 案 |
| 經 AMF | #5（NTT DOCOMO、Nokia）、#39（Tejas）、#35 b 案（Samsung）、#7（SSMF 經 NGAP，共同提案方 NTT DOCOMO）；SE 發現經 AMF 的 #13、#17 |

**對 Ericsson 統計的提醒**：Ericsson 統計 22 個 solution 走直連、8 個經 AMF（S2-2600783 Obs.1），和本站先前依 solution 數所做的分類（直連 4、經 AMF 6）差很多。差別在分類口徑：Ericsson 把所有「沒寫經 AMF」的 solution 都算成直連。這是立場文件的計法，只能參考。

---

## 3. 爭點二：感知資料路徑

| 路線 | 代表 solution | 機制 | 優點 | 缺點 | 結果 |
|---|---|---|---|---|---|
| 經 AMF 控制面 | #5 | 感知資料經 AMF 送 SF，"The N1/N2 interface may need to be enhanced" | 不必新建介面 | 原始量測量大，控制面不適合承載；AMF 負擔大 | #172 出局 |
| 重用資料框架 | #7（DCCF）、#24（SDCF） | 由資料收集協調功能匯集多台 SE 的資料 | 可以借用 R17/18 的資料收集框架 | 多一個 NF；#169 主席已刪除 NWDAF/ADRF 儲存描述 | #171 出局（P1 單一 SF） |
| 直連介面 | #21（Nx 介面）；ETRI 的 NRPPa over direct（S2-2507089，併入 #22） | SF 與 NG-RAN 之間的點對點應用協定 | 和控制信令共用連線 | 協定細節交給 RAN3 | 方向採納 |
| 直連資料隧道 | #22 | 雙方交換 TEID 或 IP 位址，建立資料隧道 | 適合大量資料 | 要靠控制信令先建隧道 | 方向採納 |
| 直連感知 session | #25 | SCF 建立 gNB–SPF 的 sensing session，連線可重用 | 控制端點和資料端點可以分開 | 需要 session 管理 | 方向採納 |
| 資料連線＋綁定 | #18 | SF 給出連線資訊與綁定 ID，SE 建立資料連線後回報綁定資訊 | UE 也適用（PDU Session） | — | 方向採納（UE 部分出局） |

- **技術核心**：結論採「控制和資料端點可以不同」（§8.4 第 2 點），以及「交換連線資訊後建立直連」（§8.4 第 3 點）。這等於同時吸收了 #25 的端點分離和 #18、#22 的「先交換連線資訊」。實際用隧道、session 還是 NxAP 承載，留給 RAN3（§8.4 NOTE 3）。
- **另一條支撐**：架構需求 ¶400 要求 "differentiation of sensing data in 5GC from other user plane traffic, for accounting / charging purposes"。直連的專用連線天生滿足這一條。這是分析，不是 TR 寫明的決策理由。

---

## 4. 爭點三：核心網 NF 結構

| 路線 | 代表 solution | 核心主張 | 結果 |
|---|---|---|---|
| 單一 SF，內部可分 SCF／SPF | #3 | "The Sensing Function may be split into Sensing Control Function and Sensing Processing Function" | **採納**（P1），但 SCF 與 SPF 之間 "no standardized interface"（NOTE 2） |
| 控制與處理分成兩個 NF，之間有標準介面 | #19（SeMF/SPF/SPAF）、#24（SSMF/SDCF）、#12（SCF/SDF/SDR） | 處理端可以獨立擴充、獨立部署 | 只保留成 SF 內部的部署選項（NOTE 3） |
| 多個處理端串接 | #23（Apple） | 為了專有融合演算法或外部 AI/ML 模型，"multiple Sensing Processing Functions (SePF) are supported"，並可串接 | 出局（P5：一個請求只選一個 SF） |
| 閘道型 NF | #10（Sensing Gateway）、#34（GSF：SF 選擇、授權、曝露、路由、計費）、#31（中央 GSMF＋分散 SSMF） | 在 NEF 和 SF 之間多一層，負責選擇、授權與計費 | 出局（§8 只剩 NEF＋SF） |
| 重用分析類 NF | #7（"possible analytics functions (e.g. NWDAF/ADRF) for processing or storing"） | 借用 NWDAF/ADRF | #169 主席當場刪除 |

- **技術核心（分析）**：
  - 分成兩個有標準介面的 NF，好處是多廠商可以互通，代價是規格量和介面數。
  - P1 NOTE 2 是折衷：允許切分，但切分只是部署方式，不標準化中間的介面。這把 #19、#24、#12 的「獨立 NF」降格成 SF 的內部實作。
  - 閘道型 NF 和 NEF 的曝露、授權功能重疊。#172 定案後只剩 NEF＋SF 兩層，閘道路線就沒有位置了。

---

## 5. 爭點四：SE（gNB）的發現與資訊來源

| 路線 | 代表 solution | 機制 | 結果 |
|---|---|---|---|
| 經 AMF 匯整 | #13、#17、#39 | SE 向 AMF 登記感知能力，SF（或 SEMF）向 AMF 訂閱或查詢。#17 的設計同時適用 "both NG-RAN and UE" | 未採；#169 已加 EN："how SE(s) provides the sensing capabilities to AMF and how and where the information is stored is FFS"（#17） |
| SE 向 SF 登記，SF 自持清單 | #15、#16 | "The Sensing Entities register/deregister to the SF and the SF keeps an inventory"（#15） | 部分採納：SF 依 supported sensing area 選 SE（§8.3 第 6 點） |
| OAM 預先設定 | — | — | 和信令並列成 FFS（§8.3 NOTE 1） |

- **細一層的分歧（#16）**：#16 設計了兩種選擇粒度。
  - Option 2：SF 直接選定 SE 與感知模式，適合靜態、大範圍的目標。
  - Option 1：SF 只選一個主 SE，再由它選發射點和接收點，因為 "the SF may not know the exact radio conditions"。
  - 結論 §8.4 第 1 點讓 gNB 自行決定量測方式，**實質上偏向 Option 1 的精神**（推論）：SF 管「要什麼」，RAN 管「怎麼量」。
- **和 AMF 之爭的連動**：控制改直連後，「經 AMF 匯整 SE 能力」就失去天然的落腳處。但 CEWiT 主張的「AMF 已經掌握 gNB 狀態」（S2-2600982 §1.2.3）並沒有被正面回應。§8.3 NOTE 1 仍是 FFS，是規範階段可能重啟的爭點。

---

## 6. 爭點五：儲存

- **需求面**：AT&T 的 S2-2505808 在 #169 被同意，架構需求 ¶399 寫 "Sensing architecture should allow for caching and/or storage and/or retrieval of sensing data"。
- **方案面**：
  - #12 的 SDR（資料庫）
  - #26 的 SDMF：儲存一段時間的結果，用來預測無人機軌跡
  - #31 的結果儲存 NF：有現成結果就直接重用
  - #38 的 SDM：儲存授權資訊，讓 AF 可以佈建
- **結論**：P2 "No dedicated storage NF is needed"。
- **技術核心（分析）**：P2 否定的是「專用 NF」，不是「儲存」本身。需求 ¶399 仍然有效，所以快取與重用可以留在 SF 內部實作。這樣可以避免在 Rel-20 定義一個新的資料儲存庫，以及它衍生的隱私與保存期限問題（這些要和 SA3 協調）。

---

## 7. 爭點六：授權細節

| 子題 | 路線 | 結果 |
|---|---|---|
| 授權資料放哪裡 | SF 本地，以 OAM 設定（#8、#37）／獨立的政策 NF SPF（#9）／UDR 或 CCF 條件檢查（#11）／AF 經 SDM 佈建（#38） | 採 SF 本地＋OAM 或預先設定（§8.2 c） |
| 緊急覆寫 | #10 的 Authorization Override Indicator（"Override" 時不檢查授權資料） | 未採 |
| 運作中重新授權 | #11（追蹤類服務可能持續一段時間） | 未採；只保留 SF 撤銷（§8.2 d） |
| 撤銷的觸發 | SF 端（#11）／gNB 端，例如目標接近禁止區（#36） | SF 撤銷、AF 取消已採納；pause 是 FFS（§8.2 NOTE 3） |
| 部分授權 | — | FFS（§8.2 NOTE 2） |

- **技術核心（分析）**：結論選了最小可行版本：靜態的 AF 授權資料表，內容是 AF ID、允許／禁止區域、允許時段、服務類型（Table 8.2-1）。動態條件（#11）、外部佈建（#38）、緊急覆寫（#10）都讓位給規範階段。

---

## 8. 爭點七：UE 當感知實體。未來會不會加回來？

### 8.1 判斷

**很可能，而且最可能在 6G。** 5G-A 的後續版本也有可能，但證據較弱。

### 8.2 支持「會回來」的證據

1. **Stage 1 需求本來就包含 UE。** TS 22.137：
   - §3.1 定義發射端與接收端都是 "part of a RAN node or a UE"
   - §5.2.1 要求沒有 5G 覆蓋的 UE 可以用免授權頻譜做感知，V2X UE 可以在不受 RAN 服務時做感知
   - §7.1 規定 6G 系統 "analogously" 適用全部 5G 需求
2. **Rel-20 的排除是範圍決定，不是技術否決。**
   - v0.2.0 §1 的 Editor's note："Any UE/RAN aspects will be aligned with TSG RAN after TSGs#108"
   - v0.3.0 範圍改為 gNB-based，並註明 "aligned to the Rel-20 5G-A RAN ISAC study scope"
   - Rel-20 的 SA2 只是跟著 RAN 的研究範圍走
3. **6G 架構研究已經把 UE 參與列成 key issue 項目。**
   - TR 23.801-01（6G 架構研究）的 WT#4 是 ISAC；KI 文字在 #172 由 S2-2511201 核准（Apple、MediaTek、LG、CEWiT、Tejas）
   - #173 已出現 KI#20 的文件，其中 KDDI 的 S2-2600305 標題是 "[KI#20, bullet#2] Investigating Architectural Challenges for UE Involvement in Sensing Operations"
   - 依標題判斷，UE 參與是 KI#20 的第二點。KI 原文尚未下載核對
4. **落敗陣營已經預留了論點。**
   - S2-2600619（Nokia、NTT DOCOMO、Samsung、KPN、Tejas）："While sensing is being scoped in R20 to only gNB based sensing, it should be considered that UEs may be in the scope of future releases"
   - S2-2600982（CEWiT、Tejas）："forward compatibility of future sensing services in 6G, where UE will also be a sensing entity"
5. **39 個 solution 裡已經有現成的 UE 路徑設計。**
   - #1：UE 當 SE 時，先經 Namf_Communication_N1N2Transfer 下發，再建立 user plane 上的直接介面，並以 LPP 為例
   - #2：UE 以專用 S-NSSAI/DNN 建 PDU Session 連 SSF，借用 TS 23.273 §6.18 的 LMF user plane 連線機制
   - #18：UE 以 PDU Session 建立資料連線，參照 LCS-UP 的建立程序
   - #17：發現與選擇程序 "common for … both NG-RAN and UE"
   - #19：SE 不限類型，消費者可以是 UE
   - #7：向 UDM 取 UE 同意與能力資訊
6. **WLAN 已經這樣做了。** 802.11bf 的非 AP STA 可以當 sensing responder 或 SBP initiator（見 802.11bf 報告 §2.1）。

### 8.3 回來時的預期樣貌（推論，只依附上列 solution）

- **控制面**：通往 UE 的控制路徑只有 NAS（經 AMF）。所以 gNB 維持直連、UE 經 AMF 的**混合架構**幾乎不可避免，Nokia 陣營的 "single approach for both UEs and gNBs" 論點會再被提出。Rel-20 的 Working Agreement 只約束 "the Sensing WID KI#1"，不約束 6G。
- **資料面**：最可能沿用 #2、#18 的 PDU Session 路線，類比 LCS-UP。
- **發現**：#17 的「NG-RAN 與 UE 共用」設計可能復活。
- **授權**：需要 UE 同意（#7 的 UDM 路線），也就是 TS 22.137 §5.2.4 的要求。

### 8.4 阻力

- UE 隱私與同意機制要和 SA3 協調。
- UE 功耗：TS 22.137 §5.1 有節能要求。
- UE 感知訊號要等 RAN1 定義。
- 跨 UE 的同步。
- 6G 的 RAN–CN 介面可能整體改變。CEWiT 的文件就提到 "RAN over SBI" 的可能，屆時「經 AMF 或直連」的二分法可能不再成立。

---

## 9. 對 SEP 實務的意義（推論）

1. **Rel-20 的 TS 會落在「直連、單一 SF、gNB 自決量測」這套組合上。** 要比對 essentiality 時，直連控制與資料連線的建立程序（§8.4 第 3 點）、SCF／SPF 的端點分離（§8.4 第 2 點）、SF 依 sensing area 選 gNB（§8.3），會是 Rel-20 專利比對的重點要件。
2. **落敗的 AMF 路線（#5、#7、#13、#17、#39）相關的專利申請，在 Rel-20 很可能不會被讀入。** 但如果 6G 把 UE 拉回來，相同機制可能以「UE 經 AMF」的形式重新變得相關。這類專利家族要追蹤 6G 版本，不宜只依 Rel-20 判斷價值。
3. **各爭點在規範階段仍留著 FFS 的部分**：SE 資訊來源、部分授權、pause、資料格式。這些是之後各公司還會再提案的地方，可能是新一輪專利申請集中的範圍。
