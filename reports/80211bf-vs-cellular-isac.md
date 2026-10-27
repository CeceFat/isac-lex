# IEEE 802.11bf（WLAN sensing）對 cellular ISAC 的啟發與影響

- 日期：2026-10-27
- 比對基準：
  - IEEE Std 802.11bf-2025（Approved 2025-05-28，Published 2025-09-26；IEEE Xplore 授權文件，本站不附原文）
  - 3GPP TR 23.700-14 v20.0.0 的 39 個 solution 與 §8 結論
- 推演紀律：所有「預期」只從 39 個 solution 已出現的機制往下推，不另創設計。每一條預期都標出它所依附的 solution 編號。
- 引用座標：802.11bf 以「條號＋PDF 頁」標示；TR 以 ¶（v20.0.0 抽文字時的 paragraph index）或 solution 條號標示。802.11bf 是 IEEE 授權文件，本報告只做極短摘引，其餘改寫，需要原文請依座標回查。

---

## 0. 結論先講

1. **兩者是同一個問題的兩種分層答案。** 802.11bf 把感知做成兩台設備之間的 MAC 層程序：能力交換 → 量測 session 協商 → 量測交換 → 終止。TR 23.700-14 則把感知做成核心網服務：AF → NEF → SF → gNB，量測細節交給 RAN WG。所以 802.11bf 對 SA2 結論的直接參考價值有限；**真正會發生交集的地方，是 RAN3 正在補的 gNB–SF 介面**（¶2969、¶2973、¶3005 都把細節交給 RAN WG3）。
2. **TR 23.700-14 全文沒有引用 802.11 或 WLAN**（關鍵字命中 0）。802.11bf 在 2025-05-28 核准，剛好是 SA2#169 Sol #1–#20 進場的同一個月。兩邊的設計大致是平行演化。
3. **最值得注意的落差有四個。** 這四個機制 802.11bf 都已經定了，TR 卻只留成 FFS 或被排除，而且 39 個 solution 裡都有對應的雛形：
   - **協商三態**：接受／帶建議參數拒絕／拒絕並設冷卻期。TR 只有 proceed／reject 兩態，partial authorization 是 FFS（¶2942–2944）。
   - **由 STA 委託 AP 代為感知（SBP）**。TR 把「UE 作消費者」排除在 Rel-20 外（Sol #2、#19、#33；¶2991）。
   - **量測層門檻觸發回報（CSI variation threshold）**。TR 的事件觸發停在結果層（物體進出區域），沒有 gNB 端的資料層門檻（Sol #27、#33、#36）。
   - **session 的隱式終止（expiry timer）**。TR 有 Sensing Service ID 與撤銷程序（Sol #11），但沒有逾時終止。
4. **反面限制。** 802.11bf 很多機制是為了「回應端是獨立、會省電、可能不在場的設備」而設計，例如 availability window、輪詢確認在場。cellular 的感知實體是業者自己的 gNB，TR 明寫 gNB 不需要授權（¶2952 f）。所以這一類機制**不該期待移植**，否則就是天馬行空。
5. **SEP 角度（推論）。** 802.11bf 從 2025-09-26 起就是公開的書面先前技術，草案更早。cellular ISAC 專利中，凡是請求項落在「帶建議參數的感知協商」「門檻觸發回報」「代理感知」的，都要拿 802.11bf 及其草案來檢驗新穎性和進步性。反過來，在 implementer 席，同一份 802.11bf 先前技術也是防禦工具。

---

## 1. 802.11bf 架構速覽（element-level）

| # | 要素 | 802.11bf 規定（改寫） | 座標 |
|---|---|---|---|
| B1 | 四個程序 | sensing procedure、SBP procedure、DMG sensing、DMG SBP | 4.11（p.27） |
| B2 | 兩組角色 | 「發起／回應」（initiator／responder）和「發射／接收」（transmitter／receiver）是兩個獨立維度；發起端甚至可以兩者都不是，只收報告 | 11.55.1.1（p.136） |
| B3 | 生命週期 | 能力交換 → 一或多個量測 session → 每個 session 多次量測交換 → 終止 | 11.55.1.1（p.136） |
| B4 | 能力交換 | 能力元素放在 Probe／(Re)Association 訊框；含 Max Supported Sessions、Responder Needed 等 | 11.55.1.3（p.138）；9.4.2.332 |
| B5 | Session 協商 | Request 帶參數，Response 回三種狀態碼之一：SUCCESS、REJECTED_WITH_SUGGESTED_SENSING_PARAMETERS（附建議參數）、REQUEST_DECLINED（附 Decline Duration 冷卻期） | 11.55.1.4.1（p.140、p.143） |
| B6 | Session 參數固定 | 參數在 session 期間固定，以〈發起端 MAC, Measurement Session ID〉識別 | 11.55.1.4.1（p.140–141） |
| B7 | 隱式終止 | 雙方各自啟動 session expiry timer，每次量測交換後重置，逾時即終止 | 11.55.1.4.1（p.143–144）；11.55.1.6（p.164） |
| B8 | 可用時窗 | 回應端宣告可用時窗與偏好週期（以 10 TU 為單位，須是 beacon interval 的倍數），AP 指派重疊的時窗；時窗內優先做感知 | 11.55.1.3（p.139）；11.55.1.5.2.1（p.147） |
| B9 | 量測交換 | TB 版由 AP 觸發：polling → NDPA sounding → TF sounding → reporting；另有 non-TB 版 | 11.55.1.5.2（p.146–147）；11.55.1.5.3 |
| B10 | 門檻觸發回報 | 回應端先回報 CSI 變化量，超過 AP 指派的門檻才被排程送完整報告，目的是降低回報負擔 | 11.55.1.5.2.6.2（p.156–157） |
| B11 | 量測品質中繼資料 | 接收端回報 Rx 工作點／增益索引，標示 CSI 估計受非線性影響的程度 | 11.55.1.5.5（p.163） |
| B12 | 終止 | 任一方隨時可明確終止；BSS 參數變動時，AP 必須終止與未關聯 STA 的 session | 11.55.1.6（p.164） |
| B13 | SBP（代理感知） | 非 AP 的 STA 請 AP 代為感知。可指定偏好回應端、所需回應端數量（硬性或軟性）、門檻回報、時間戳；AP 另起一個新的感知程序去滿足請求，再把報告轉給請求方；SBP 終止會連帶終止底下的 session | 11.55.2（p.165–172） |
| B14 | DMG 感知類型 | 單站、雙站、多站、協調單站（AP 協調多台設備各自做單站）、協調雙站、被動（借 beacon）；以 burst 結構累積 Doppler 量測 | 11.55.3.1（p.173–174） |
| B15 | 報告粒度 | sub-7 GHz 回報 CSI；DMG 的 Report Type 可選 CSI、各種感知影像（range-Doppler 等），甚至直接回報目標清單（Target） | 9.4.1.81；Table 9-417ad（p.92）；9.4.2.341.4 |
| B16 | 安全 | AP 要求時，未關聯 STA 必須先用 PASN 建立 PTKSA 才能發起 session；否則感知訊框一律丟棄 | 11.55.1.2（p.137） |

---

## 2. 逐項對照：802.11bf 機制 × TR 23.700-14 × 39 solutions

欄位說明：「TR 現況」以 §8 結論為準；「最接近的 solution」只列 39 個裡真的出現過的；「預期」是推論，不是事實。

### 2.1 代理感知（B13 SBP）↔ 感知即服務

- **對應關係**：802.11bf 的 SBP 是「沒有感知控制權的一方，請有控制權的一方代為感知，再把報告轉回來」。TR 的 AF → NEF → SF → gNB 是同一個模式，只是代理人換成核心網。這一層已經採納（¶2980–2987）。
- **落差**：SBP 的請求方是終端設備。TR 在 Rel-20 只承認 AF 為消費者（¶2991 NOTE 4："It is assumed that a sensing service requester and a sensing service consumer is the same entity"），讓 UE 當消費者的 Sol #2（UE 經 PDU Session 連 SSF）、Sol #19（SSC 可為 UE）、Sol #33（UE 發起請求，依訂閱資料授權）都沒進結論。
- **啟發**：802.11bf 證明「終端請求、網路代測、報告回傳」可以用很輕的協定標準化。SBP 只有 Request／Response／Report／Termination 四種訊框。
- **預期（推論）**：後續版本如果放寬範圍，最可能復活的是 Sol #2（user plane＋slice 授權）或 Sol #33（以 UE 訂閱資料授權）的路線，而不是新設計。Sol #2 自己就說它借用 LMF 的 user plane 連線機制（¶526），工程成本最低。

### 2.2 協商三態（B5）↔ 授權只有兩態

- **TR 現況**：SF 授權後只有兩種結果，"proceeds the Sensing Service Request"（¶2942）或 "rejects"（¶2943）。¶2944 把 partial authorization 留到規範階段。
- **最接近的 solution**：
  - Sol #19：SPAF 會檢查 "availability of resources, Sensing Entities, etc."（¶1623）。這是可行性驗證，但只回答可不可以，不會反提案。
  - Sol #6：依 SE 能力授權。
  - Sol #11：運作中重新授權。
- **啟發**：802.11bf 的 REJECTED_WITH_SUGGESTED_SENSING_PARAMETERS 是一個現成的 partial authorization 樣板：拒絕原請求，但附上做得到的參數，由請求方決定要不要重送。REQUEST_DECLINED 再配一個 Decline Duration，可以防止請求方反覆重送。
- **預期（推論）**：¶2944 在規範階段若要落地，最省事的做法是在 Sol #19 的可行性驗證上，加一個「建議 Sensing QoS／時間參數」欄位。可協商的欄位應該就是 ¶2987 列的那幾項：target sensing service area、sensing time parameters、requested Sensing QoS。

### 2.3 Session 識別、參數固定與隱式終止（B6、B7）

- **TR 現況**：§8 沒有 session 生命週期的規則。§8.6 只有 "Sensing service duration"（¶3002）。
- **最接近的 solution**：
  - Sol #11：在 v0.3.0 新增撤銷程序，原文 "Sensing Service ID is defined to uniquely identify the ongoing Sensing Service in core network"（§6.11.2.3）。這是 39 個裡**唯一在進場後被實質擴寫**的 solution（見 [版本溯源報告](version-trace.md)）。
  - Sol #25：直連 "may maintain the established direct connection, which can be reused"。
- **啟發**：802.11bf 的雙方逾時計時器解決的是「一方消失、另一方不知道」的問題。SF 與 gNB 改成直連、不經 AMF（¶2930–2931）之後，就少了 AMF 這個狀態錨點，連線與 session 的存活確認更需要明文規定。
- **預期（推論）**：規範階段會在 Sol #11 的 Sensing Service ID 上，補「持續時間到期即自動釋放」的語意，並沿用 Sol #25 的連線重用。不會整套引進 802.11bf 的 keep-alive，因為 gNB 不會像 STA 那樣離開。

### 2.4 可用時窗（B8）——不應期待移植

- 802.11bf 需要 availability window，是因為回應端是會睡眠、會離開的 STA，AP 得先排好大家都醒著的時間。
- cellular 的感知實體是業者自己的 gNB。TR 明寫 "There is no need for authorization for the gNB as the Sensing Entity, as the gNB is deployed by operator"（¶2952 f），而且量測怎麼做由 gNB 自行決定（¶2968）。
- 39 個裡唯一碰到資源可用性的是 Sol #6：SE 因過載或能耗上限不可用時，SF 就不選它（¶808）。這是**選擇時排除**，不是**協商時窗**。
- **結論**：時窗協商留在 RAN 內部，SA2 不會標準化。只有時間參數這一層會跨介面：Sol #27 的 start／end／duration（¶1975）、Sol #33 的 periodicity（¶2426），以及 §8.6 的回報型態（¶3004）。

### 2.5 門檻觸發回報（B10）↔ 事件觸發

- **TR 現況**：§8.5 有一次／週期／事件三種（¶2986），事件內容是 Sensing service type，例如 "object in/out of a defined area"（¶2989）。這些都是**結果層**事件，在 SF 算完之後判斷。
- **最接近的 solution**：
  - Sol #27：速度超過門檻才送結果（¶1991）。
  - Sol #33：物體進入或離開目標區域。
  - Sol #36：**由 gNB 端**偵測到物體接近禁止區，主動請 SF 暫停或撤銷（¶2647）。
- **啟發**：802.11bf 把門檻放在**量測層**：接收端先算 CSI 變化量，沒超過門檻就不上傳完整量測，省的是空口和回傳頻寬。對應到 cellular，就是 gNB 在送感知資料給 SF 之前先做資料層的門檻過濾。
- **預期（推論）**：這會是 RAN3 定義感知資料回報時的議題，因為 §8.4 NOTE 4 把回報型態交給 RAN WG（¶2975）。SA2 層的事件觸發會照 §8.5 停在結果層。gNB 端觸發目前只有 Sol #36 一個雛形，而且 pause 仍是 FFS（¶2945）。

### 2.6 報告粒度：原始量測 vs 目標清單（B15）

- **TR 現況**：結果由 SF 產生（¶2977、¶2980）。感知資料的格式交給 RAN WG3（¶2969）。
- **最接近的 solution**：
  - Sol #19：明寫可選 "the option of having the processing functionality at the SE"。
  - Sol #1：允許 SE 把資料或結果直接送給消費者（¶487）。
  - 兩者都沒進結論。
- **啟發**：802.11bf 在同一個標準裡同時支援三種粒度：原始 CSI、處理過的感知影像（range-Doppler 等）、目標清單。差別交給 session 協商時的 Report Type 決定。這代表「gNB 上傳什麼」不必二選一，可以變成 session 參數。
- **預期（推論）**：RAN3 會出現「上傳原始量測」與「上傳目標層結果」之爭。SA2 結論把結果產生放在 SF，但 ¶2968 讓 gNB 自己決定怎麼量，所以這個口子是開著的。Sol #19 的「處理放在 SE」選項，可能以 RAN3 回報型態的形式回來。

### 2.7 量測品質與時間戳（B11、B13 Report Timestamp）↔ Sensing QoS 資訊

- **TR 現況**：結果可以包含 "Sensing QoS information, Sensing timestamp"（¶2983）；NOTE 2 說 Sensing QoS 的術語與細節到規範階段再定（¶2985）。
- **最接近的 solution**：Sol #30 的 contextual information 包含 "timestamp, accuracy estimation, confidence level"（¶2211）；Sol #7 有 "optional confidence metrics or timestamps"（¶858）。
- **啟發**：802.11bf 的 Rx 工作點索引是**量測端自報品質**的做法：接收端說明這次估計受硬體狀態影響多大，讓處理端決定權重。對應到 cellular，就是 gNB 隨感知資料附上的 "associated information"（¶2974）可以裝什麼。
- **預期（推論）**：Sensing QoS 資訊會分成兩層。SF 對 AF 的部分沿用 Sol #30 的信心水準和準確度；gNB 對 SF 的部分由 RAN3 決定，有可能加入類似量測品質指標的欄位。

### 2.8 多實體協調（B2、B14）↔ 一個 SF 選多台 gNB

- **TR 現況**：同一個請求可以向一或多台 gNB 收資料（¶2976），由 SF 選擇與重選 gNB（¶2962–2963），只選一個 SF（¶2932）。
- **最接近的 solution**：Sol #39（單站感知，經 AMF 設定，已落敗）；Sol #24 的 SDCF 匯集多台 SE（已落敗）。
- **啟發**：802.11bf 的「協調單站」（一個 AP 協調多台各自做單站的設備）在結構上最接近 TR 的結論：SF 協調多台各自做單站感知的 gNB，再自己融合。至於雙站、多站需要的跨設備時間同步，802.11bf 交給 PHY／MAC 處理，cellular 則屬 RAN1／RAN3。
- **預期（推論）**：Rel-20 SA2 層面會停在「協調單站」型態；雙站／多站要等 RAN 研究，SA2 只需要讓一個請求對應多台 SE。

### 2.9 終止與撤銷（B12）

- **TR 現況**：SF 可以在條件不再滿足時撤銷（¶2950）；AF 可以取消，SF 隨後終止和 SE 之間的作業（¶2951）。
- **最接近的 solution**：Sol #11（SF 撤銷，SE 可以 "terminate or temporarily deactivate"）；Sol #36（gNB 主動請求暫停或撤銷，附原因值）。
- **啟發**：802.11bf 允許**回應端**主動終止，並且在網路參數改變時強制終止。對應到 cellular，就是 gNB 主動告知「這個感知任務做不下去了」，例如目標離開覆蓋或 cell 重新設定。
- **預期（推論）**：gNB 發起的終止或通知會以 Sol #36 的原因值形式進入規範。pause 是否標準化仍看 ¶2945。

### 2.10 能力交換（B4）↔ SE 資訊來源

- **TR 現況**：SF 怎麼取得 SE 資訊（經 OAM 或經信令）未決（¶2964）；SE 能力的細節也未決（¶2965）。
- **最接近的 solution**：Sol #15、#16（SF 自持清單／SE 向 SF 註冊）；Sol #13、#17、#39（經 AMF 匯整，與 P4a 的直連方向不一致）。
- **啟發**：802.11bf 的能力元素明列「最多同時幾個 session」。這種「並行感知任務上限」對 SF 選 gNB 很實用，目前 TR 的選擇準則只提到 supported sensing area（¶2962）。
- **預期（推論）**：既然控制信令已改直連，SE 資訊會傾向經直連介面或 OAM 取得（Sol #15、#16 路線），經 AMF 匯整（Sol #13、#17）的機會下降。並行容量這類能力欄位可能出現在 RAN3 的能力定義裡。

### 2.11 安全（B16）

- 802.11bf 對未關聯設備強制先建金鑰。TR 把隱私與安全全部交給 SA3（¶2933 NOTE 5、¶2993）。Rel-20 只有 gNB 一種感知實體，而且是業者自己的設備，沒有「未關聯設備」的問題。
- 這一點**不構成移植需求**。若日後 UE 被納入（見 2.1），802.11bf 的未關聯 STA 規則才會有參考價值。

---

## 3. 總表

| 802.11bf 機制 | TR 23.700-14 現況 | 最接近的 solution | 移植預期 |
|---|---|---|---|
| SBP 代理感知 | AF 代理已採納；UE 消費者排除 | #2、#19、#33 | 中：後續版本放寬範圍時 |
| 協商三態＋冷卻期 | 兩態；partial authorization FFS | #19、#6、#11 | **高**：規範階段補 ¶2944 |
| Session ID／參數固定 | Sensing service duration | #11 | 中：補到期釋放語意 |
| 隱式終止計時器 | 無 | #25（連線重用） | 低到中 |
| 可用時窗 | gNB 自決量測 | #6（只做選擇排除） | **不移植** |
| 門檻觸發回報（量測層） | 結果層事件已採納 | #27、#33、#36 | 中：在 RAN3 層 |
| 報告粒度可選 | SF 產生結果；資料格式交 RAN3 | #19、#1 | 中：在 RAN3 層 |
| 量測品質／時間戳 | Sensing QoS、時間戳已列入 | #30、#7 | 高：已有方向 |
| 協調單站 | 一 SF 多 gNB | #39、#24 | 已大致吻合 |
| 回應端主動終止 | SF 撤銷、AF 取消 | #36、#11 | 中 |
| 能力含並行上限 | SE 資訊來源 FFS | #15、#16 | 中 |
| 未關聯設備安全 | 交 SA3 | — | 不適用（Rel-20） |

---

## 4. 對 SEP 實務的影響（推論，需另行驗證）

1. **先前技術日期。** 802.11bf-2025 在 2025-09-26 出版，是確定的書面公開日。TGbf 的草案與會議文件更早公開，實際最早日期要另查 IEEE 802.11 TGbf 文件庫。TR 23.700-14 的 solution 在 2025-05（SA2#169）和 2025-08（SA2#170）進場，所以兩邊的先後要逐案比較。
2. **高重疊區。** 若有 cellular ISAC 專利的請求項落在下列機制，應先拿 802.11bf 及其草案檢驗新穎性和進步性：
   - 感知請求被拒時回傳建議參數（B5 ↔ 2.2）
   - 依量測變化量門檻決定是否上傳（B10 ↔ 2.5）
   - 終端委託網路代為感知並轉回報告（B13 ↔ 2.1）
   - 回報型態可選原始量測或目標清單（B15 ↔ 2.6）
3. **反向風險。** 802.11bf 本身也可能有 SEP 宣告。同時出貨 Wi-Fi 與 5G 產品的 implementer，可能在兩個標準各自面對授權主張。本報告沒有查任何 802.11bf 的 LoA 或專利宣告。
4. **essentiality 時點。** cellular 這一側目前只有 TR，不能做 essentiality 判斷。要等 Rel-20 Stage 2 TS 和 RAN3 Stage 3 出來，才能逐要件比對。

---

## 5. 限制

- 802.11bf 只精讀了 4.11、11.55.1（全）、11.55.2（全）、11.55.3.1、11.55.3.4 開頭、11.55.3.9，加上 Table 9-417ad 和 9.4.2.341.4。DMG 各量測交換細節（11.55.3.6）和 PHY 條文只看了目錄與標題，沒有逐字讀。本報告的結論不依賴那些條文；若要評估 PHY 層的專利重疊，需要補讀。
- TR 端只用 v20.0.0 的 §8 結論和各 solution 的原則段，沒有看 RAN WG 的 ISAC 研究（Rel-20 RAN 端 TR）。2.5、2.6、2.10 的預期都落在 RAN3，有待 RAN 端文件驗證。
