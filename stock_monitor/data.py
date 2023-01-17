from stock_monitor.models import Stock, Arbitrage, Expectation
from datetime import datetime, timezone
from streamlit import cache


def tickers():
    return ["TGNA", "FSTX", "KOP", "CEG", "VST", "CNQ"]


@cache(persist=False, ttl=3600, allow_output_mutation=True)
def vix_stocks(period: str, interval: str):
    return [Stock(ticker_name, period=period, interval=interval) for ticker_name in
            ["GOOG", "NVDA", "ASML", "KLAC", "WAF.DE", "MSFT"]]


@cache(persist=False, ttl=3600, allow_output_mutation=True)
def tax_loss_jan_stocks(period: str, interval: str):
    return [Stock("SLGC", period=period, interval=interval,
                  description=r"""Somalogic \$SLGC, \$2.26 - A leading platform for proteomics analysis,
                                  \$SLGC has a \$435 mm cap w/ \$550 mm+ of cash. \$SLGC has cut costs and
                                  should burn ~\$80-\$100 mm in '23, w/ a partnership with \$ILMN due to
                                  launch in '24.  New Exec Chair seems like validation."""),
            Stock("ALLT", period=period, interval=interval,
                  description=r"""Allot \$ALLT, \$2.86 - A provider of carrier networking solutions,
                                  \$ALLT's move into a new consumer facing security biz has been a disaster.
                                  Mgmt, however, now appears under pressure to rollback that effort.
                                  Core DPI biz is very strong. \$110 mm cap with good balance sheet."""),
            Stock("ACTG", period=period, interval=interval,
                  description=r"""Acacia \$ACTG, \$3.59 - Stock now trades at 68% of \$5.25 per share book
                                  value pro-forma for Starboard deal, and Viamet and Wifi 6 patents are
                                  probably worth \$1+ more per share. Balance sheet is rock solid and loaded
                                  with cash, & $ACTG has bought back a lot of stock in past."""),
            Stock("DSP", period=period, interval=interval,
                  description=r"""Viant \$DSP, \$3.34 - Trading flat with its ~\$225 mm of cash w/ breakeven
                                  operations (w/ solid EBITDA in past), \$DSP offers a buy side programmatic
                                  ad-tech platform that has nicely grown ad spend volume over the years.
                                  The two brothers who control \$DSP are solid entrepreneurs"""),
            Stock("CGNT", period=period, interval=interval,
                  description=r"""Cognyte \$CGNT, \$2.40 - This cybersecurity play had a rocky year of
                                  operations but appears to be regaining its footing with cost cuts and asset sales.
                                  Biz has been profitable in past and balance sheet is now on firmer ground.
                                  \$160 mm cap."""),
            ]


@cache(persist=False, ttl=3600, allow_output_mutation=True)
def ideas(period: str, interval: str):
    ideas = [Stock("VONOY", period=period, interval=interval,
                   expectation=Expectation(price=30, date=datetime(2024, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Germany's biggest landlord $VNA is priced at a 70% discount to its net asset value.
                                  Its share price would need to 3x just to reach its net asset value.
                                  [Source](https://twitter.com/askjussi/status/1611358663754813440)"""),
             Stock("DBRG", period=period, interval=interval,
                   expectation=Expectation(price=40, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Pure play alternative asset manager focused exclusively on network infrastructure
                                  investments. A transformed Colony Capital with nearly all legacy assets sold off.
                                  Significant step up in earnings expected in 2023 after the launch of several new
                                  funds. Market is pricing in zero success in fundraising and gives no credit for the
                                  carried interest. Sentiment is likely to reverse upon successful new fund launches.
                                  Insiders started buying stock recently. Infrastructure is a key growth engine for
                                  alternative asset managers. \$KKR, \$BX, etc., are all raising significant capital
                                  for infrastructure investments and \$DBRG is the fastest-growing manager out there.
                                  Valuing fee-related earnings at 22x, results in a SOTP valuation of \$32\/share with an
                                  additional \$5\/share from carried interest.
                                  **Exp. gain: +200\% to \$40\/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)"""),
             Stock("CRNT", period=period, interval=interval,
                   expectation=Expectation(price=3.08, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""Vendor for global wireless network operators specializing in backhaul solutions.
                                  Shareholders have recently rejected a hostile takeover by peer \$AVNW at \$3.8/share.
                                  Renewed talks between AVNW and CRNT present the potential for near-term upside
                                  realization. While \$AVNW is the leader in NA backhaul, CRNT is now encroaching on
                                  its territory, having secured contracts with every NA Tier 1 operator. AVNW used a
                                  difficult equity market environment to try to opportunistically scoop up an
                                  undervalued asset.Post proxy fight CRNT management is forced to drive shareholder
                                  value.Trades near its historical 1x book value floor. Failed takeover attempt at
                                  \$3.08/share in Aug’22. Management’s internal value estimate of \$5/share.
                                  **Exp. gain: +70% to\$3.08+**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)"""),
             Stock("SI", period=period, interval=interval,
                   expectation=Expectation(price=120, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""FDIC-regulated bank which specializes in serving the crypto-currency ecosystem and
                                  acquired the Diem platform from \$META. An institution with a very liquid asset book
                                  of government securities trading below tangible book. No credit risk exposure to
                                  crypto.The stock is down from \$220 to \$30 over the past year. At 1xBV, the downside
                                  is very well protected with material optionality from crypto recovery or Diem getting
                                  regulatory approval.Trades at 1xBV. In an upside scenario, it is a differentiated
                                  financial institution worth several multiples of BV. If Diem takes off \$SI becomes a
                                  high-growth technology company.
                                  **Exp. gain: 2x-4x.**
                                  [Source](https://twitter.com/InvestSpecial/status/1610585909128302593)"""),
             Stock("AMKR", period=period, interval=interval,
                   expectation=Expectation(price=87, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Semiconductor assembly services provider – the world’s most wonderfully boring
                                  businesses to own. At 9x earnings and shifting into higher margin services.
                                  For a semi business, it has very low cyclicality and low capex needs, and yet is
                                  delivering above-industry revenue growth with 3 year CAGR of 20%. Oligopolistic
                                  industry – AMKR is the No.2 player with a 25% share, behind \$ASX with 35%. Due to
                                  increasing chip complexity, the industry is shifting towards less commoditized and
                                  more advanced packaging/assembly solutions, requiring more R&D and tighter
                                  integration with customers. This also drives increasing margins for key players.
                                  Should trade at an above-market multiple of 20x vs 9x today. ’23 and ’24 EPS are
                                  expected at \$3 and \$4. Easy double with \$4 fwd EPS and 10.5x multiple. DCF model
                                  results in \$87/share. **Exp. gain: +100% by 2H23.**
                                  [Source.](https://twitter.com/InvestSpecial/status/1612025171879010305)"""),
             Stock("XMTR", period=period, interval=interval,
                   expectation=Expectation(price=45, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Marketplace for small batch manufacturing and prototyping. Currently trades at its
                                  Jun’21 IPO level and at 4.5x revenue, while comps are in the 1-2x range. Competitive 
                                  and low-entry barrier industry that is significantly exposed to macro headwinds. 
                                  Clients and suppliers can as easily connect directly. 
                                  No clear operating leverage with increasing scale. Relies heavily on Google Adwords 
                                  to drive traffic. Guidedown in pricing already happened with Q3’22 results, 
                                  volume might drop in 2023.Trades at 4.5x revenues, still at the IPO price vs. a comp 
                                  universe 3-D printers and short-run fabricators in the 1-2x range. **Exp. gain: 50%-75%**
                                  [Source.](https://twitter.com/InvestSpecial/status/1612387567302840320)"""),
             Stock("FIP", period=period, interval=interval,
                   expectation=Expectation(price=7, date=datetime(2023, 6, 1, tzinfo=timezone.utc)),
                   description=r"""Recent spin-off from \$FTAI with 4 infrastructure assets: 3 energy terminals and a
                                  railroad business. EBITDA is set to increase from \$140m today to \$250m in the next
                                  12-18 months. FPI’s Jefferson terminal is now on cusp of generating strong earnings.
                                  Transtar railroad earnings have been consistently increasing through new business
                                  initiatives. Construction of the 485MW power plant at Long Ridge is complete.
                                  Downside is well protected at current share price levels.Base case EBITDA is set to
                                  grow from \$140 million today to \$250 million over the next 12-18 months.
                                  At 11x multiple, the target of \$6.7/share. **Exp. gain: +130% to \$7/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)"""),
             Stock("ALIT", period=period, interval=interval,
                   expectation=Expectation(price=11, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""Provider of outsourced human capital management services/software with multiple
                                  upcoming event catalysts. Steady business, with 3-5 year contracts, 15-year average
                                  customer life, and 97% rev retention. Comp set is performing very well in the stock
                                  market.Stock was down 20% after a botched secondary offering. However, Bill Foley
                                  pulled out from selling. His lack of participation in the secondary was extremely
                                  telling. His number two, Rick Massey, subsequently bought \$840k of stock around
                                  current levelsPeers \$WTW and \$G with similar expected growth and financial profiles
                                  trade at 11x-11.5x 1-year forward EBITDA.
                                  At this multiple \$ALIT is worth \$10.5-11.0/share today.
                                  **Exp. gain: +20% to \$11/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)"""),
             Stock("ZIMV", period=period, interval=interval,
                   expectation=Expectation(price=37, date=datetime(2023, 12, 31, tzinfo=timezone.utc)),
                   description=r"""Recent spin-off from Zimmer Biomet with shares down 80% from the first day of trading.
                                  Orthopedics company offering spine surgery solutions and dental implants. Stable,
                                  65% GM business, set to benefit from post-pandemic recovery in elective surgeries.
                                  Margin improvement potential from the current 9% to 15-20% peer levels. Trades far
                                  below peer group on a revenue multiple. Trailing revenues were weak due to distortion
                                  by several transitory factors.Current EV/Sales of 0.75x is far below the peer group’s
                                  3.3x. Full-recovery EV/EBIT of around 7x vs around 15x for the peer group.
                                  At 15x multiple would be valued at \$37/share. **Exp. gain: +300% to \$37/share.**
                                  [Source](https://twitter.com/InvestSpecial/status/1613508259154984962)"""),
             Stock("BJ", period=period, interval=interval,
                   expectation=Expectation(price=140, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""**What does BJ do?** The business is a discount wholesale club like Costco but
                                   focused on a more middle-class income demographic (Costco tends to skew higher
                                   income). BJ’s charges an annual membership fee of \$55 to \$110 and delivers
                                   extreme savings of 30% on average compared to traditional grocery and general
                                   merchandise stores. This is a strong value proposition for a family that shops
                                   once or twice per month for household essentials.
                                   **Why is it a good bet?** Discount retailers tend to outperform during
                                   recessionary periods as well as inflationary periods when consumers are looking
                                   for bargains. During the 2008/2009 recession, discounters such as Dollar General
                                   posted strong sales comps. We studied several discount retail concepts this summer
                                   and determined that BJ’s presents the best longterm opportunity
                                   **Why does the opportunity exist?** With just 226 store units compared to Costco’s
                                   847 units, BJ’s has a significant opportunity to grow its store base and is
                                   currently accelerating new unit openings
                                   **What’s the prize if you’re right?** Investors appreciate the quality of the
                                   wholesale club model and have awarded Costco a 32x price-to-earnings multiple.
                                   Despite BJ’s being a ‘Costco clone’, its stock only trades for 17.5x earnings –
                                   a near 50% discount(!). [Source](https://macro-ops.com)"""),
             Stock("HLS.TO", period=period, interval=interval,
                   expectation=Expectation(price=25, date=datetime(2023, 5, 31, tzinfo=timezone.utc)),
                   description=r"""Small cap Canadian pharma with shares near all-time lows and business fundamentals
                                   finally inflecting to the positive. Investment case is mainly based on one of two
                                   HLS’s drugs, Vascepa, that is in the initial stages of commercialization.
                                   Vascepa is approved, clinically effective, and has reimbursement coverage
                                   Pfizer Canada is the team pushing things forward for commercialization
                                   Sales are growing 30%-40% QoQ and are only now approaching sufficient prescription
                                   levels to break evenThe initial Vascepa commercialization difficulties were mainly
                                   caused by Canada’s lengthy COVID lockdown.
                                   Precedent drugs suggest management's estimate of 10% penetration is overly conservative
                                   and that 20-40% levels could be reached.The already commercialized drug Clozaril alone
                                   supports current HLS valuation, implying less than zero value for Vascepa.
                                   With Vascepa roll-out, HLS is worth $25/share.
                                   **Exp. gain: +150% to $25/share.**.
                                   [Source](https://twitter.com/InvestSpecial/status/1615303074473451521)""")
             ]
    return sorted(ideas, key=lambda x: x.expectation.date)


@cache(persist=False, ttl=3600, allow_output_mutation=True)
def stocks(period: str, interval: str):
    res = []
    for ticker_name in tickers():
        buy_date = None
        if ticker_name == "FSTX":
            buy_date = datetime(2022, 11, 30, tzinfo=timezone.utc)
        elif ticker_name == "TGNA":
            buy_date = datetime(2022, 12, 1, tzinfo=timezone.utc)
        elif ticker_name == "KOP":
            buy_date = datetime(2022, 12, 6, tzinfo=timezone.utc)
        elif ticker_name == "CEG":
            buy_date = datetime(2022, 12, 6, tzinfo=timezone.utc)
        elif ticker_name == "VST":
            buy_date = datetime(2022, 12, 16, tzinfo=timezone.utc)
        elif ticker_name == "CNQ":
            buy_date = datetime(2022, 12, 19, tzinfo=timezone.utc)
        res.append(Stock(ticker_name, period=period, interval=interval, buy_date=buy_date))
    return res


@cache(persist=False, ttl=3600, allow_output_mutation=True)
def arbitrages(period: str):
    res = [Arbitrage(target=Stock(ticker_name="ATVI", period=period), buyer=Stock(ticker_name="MSFT", period=period),
                     offer_price=95, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The spread mainly exists due to regulatory
                                    concerns over MSFT's potential abuse of power and potential restriciton of ATVI
                                    games solely to Xbox console. UK and European antitrust watchdogs, among others
                                    have started their inquiries into the transaction. EU Commission has extended it's
                                    deadline for a decision til Apr'23. This month, Chinese regulators rejected the
                                    simplified filling request for the merger. Recent rumors on the merger suggest that
                                    FTC plans to block the merger. Warren Buffet's Berkshire is also participating in
                                    this merger arb play providing some confidence in the successful outcome and/or
                                    a well-protected downside on ATVI standalone basis."""),
           Arbitrage(target=Stock(ticker_name="IRBT", period=period), buyer=Stock(ticker_name="AMZN", period=period),
                     offer_price=61, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 8, 31, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The spread has widened from 5% to over 15% as market
                                started pricing in higher likelihood of regulatory hurdles. Two months ago the parties
                                received the 2nd request from the FTC. Soon after, several senators began pushing the FTC to
                                block the transaction. Concerns were raised regarding potential privacy infringements and
                                Amazon's history of anti-competitive acquisitions. FTC review is ongoing."""),
           Arbitrage(target=Stock(ticker_name="SAVE", period=period), buyer=Stock(ticker_name="JBLU", period=period),
                     offer_price=31, additional_buyer_ratio=0,
                     expecting_closing=datetime(2024, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. Bidding war for Spirit Airlines seems to have come to
                                an end. Shareholders voted for JBLU's offer. The current spread is mainly due to antitrust
                                concerns. DOJ has issued a second request and is currently reviewing the merger. That being
                                said, JBLU has proposed divertitures in overlapping areas - this could alleviate antitrust
                                concerns. Another DOJ concern relates to JBLU's Northeast parnership (NEA) with American Airlines.
                                Recently, a motion to dismiss the DOJ case against NEA has been denied. Now the decision comes down
                                to the judge's reading of antitrust law which could signifacntly delay the decision. Hence
                                SAVE-JBLU merger outcome might also depend on the outcome of NEA trial."""),
           Arbitrage(target=Stock(ticker_name="BKI", period=period), buyer=Stock(ticker_name="ICE", period=period),
                     offer_price=68, additional_buyer_ratio=0.144,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. Shareholders have already approved the merger. However,
                                Community Home Lender Association has called regulators to block the merger over antitrust
                                concerns saying that the combined company will have too much pricing power in the small/medium
                                mortgage banking sector. The companies each hold dominant market shares in speicfic US mortgage
                                software segments - servicing (BKI) and origination (ICE) - suggesting the merger will lead to
                                substantial vertical integration. Recently ICE agreed to an extended FTC review with reiterating
                                its expectation merger completion by H1'23
                                """),
           Arbitrage(target=Stock(ticker_name="FSTX", period=period), buyer=Stock(ticker_name="1177.HK", period=period),
                     offer_price=7.12, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 1, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The market seems to be concerned that the merger
                                might get blocked by CDIUS due to the buyer being a Chinese firm. Such regulatory
                                concerns are quite unusual given this is a tiny acquisition of an oncology treatment
                                developer with a very early-stage pipeline. However, a couple of weeks ago, parties had
                                to withdraw and refile the merger documents to CFIUS. As a result of this, the
                                transaction end date was extended till the 19th Dec. Downside to pre-announcement price
                                is very steep, which also partally explains the spread.
                                """),
           Arbitrage(target=Stock(ticker_name="TGNA", period=period),
                     buyer="Standard General", offer_price=24.15,
                     additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 2, 28, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The buyer consortium includes Standard General,
                                Apollo, and Cox Media. Various industry players and unions have voiced their concerns
                                that combined TGNA/Cox Media will control too much of the market share (39% of U.S. TVH)
                                Other concerns include potential staff reductions, lower local news coverage and
                                renegotiations of retransmission fees. Analsis of TGNA and Cox Media's US household
                                coverage suggests that the combined company would still be withing the limits of FCC
                                ownership rules, whereas the merger will not affect competition. Recently Telecom
                                regulators noted they have no objections to the merger. However, both FCC and DOJ
                                reviews are still ongoing. Merger end date has now bee extended till Feb'23.
                                """),
           Arbitrage(target=Stock(ticker_name="TSEM", period=period), buyer=Stock(ticker_name="INTC", period=period),
                     offer_price=53, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 12, 31, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The merger will require numerous antitrust
                                and foreign investment approvals. Intel's CEO has noted that regulatory clearance has
                                already been received in several geographies. The transaction continues to be held up
                                by Chinese regulators, which have been increasing scrutinty over the merger in a
                                strategically important semiconductor space. For the same reason there is uncertainty
                                regarding Israel's government approval. Israel withholding taxes will apply in case of
                                succesfull closing - to avoid tese foreign investors will be required to provide some
                                paperwork, which might delay the eventual payout of the merger consideration and might
                                explain part of the spread.
                                """),
           Arbitrage(target=Stock(ticker_name="VMW", period=period), buyer=Stock(ticker_name="AVGO", period=period),
                     offer_price=71.25,
                     additional_buyer_ratio=0.125,
                     expecting_closing=datetime(2023, 10, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - long timeline/regulatory review. This is mammoth \\$61bn deal,
                                giving Broadcom a push into the software industry. A long and detailed probe from EU
                                regulators is expected. Broadcom's CEO has noted that regulatory filings have so far
                                seen good progress in numerous grographies. The merger could take more than a year to
                                complete.
                                """),
           Arbitrage(target=Stock(ticker_name="ACI", period=period), buyer=Stock(ticker_name="KR", period=period),
                     offer_price=27.25, additional_buyer_ratio=0,
                     expecting_closing=datetime(2024, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. US senators have raised anticompetitive concerns
                                to the FTC. To satisfy potential regulatory hurdles ACI and KR proposed divesting a
                                large number of stores. Also, as part of the merger agreement, ACI had to pay a
                                \\$6.85\\/share special dividend to its shareholders. However, several states filed a
                                lawsuit to block the payment arguing it would weaken the company's ability to compete
                                as the antitrust reviews proceed. Court's hearing has now been delayed till the 9th Dec.
                                Management remains confident that divestments will be enough to satisfy potential
                                regulatory concerns while also stating that a lawsuit related to divident payments is
                                groundless and should ger resolved in court.
                                """),

           Arbitrage(target=Stock(ticker_name="SIMO", period=period), buyer=Stock(ticker_name="MXL", period=period),
                     offer_price=93.54,
                     additional_buyer_ratio=0.388,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - Chinese regulatory approval. Approval from China's regulators is the main hurdle.
                                The buyer is based in the U.S, while the target is a US-listed Taiwanese company with China being
                                its largest market. Both parties had previously filed under the simplified procedures, but have
                                now re-filed under a normal procedure as advised by Chinese regulators. This month the documents
                                have been accepted and regulatory review is underway.
                                Management reiterated the expected closing date to be in mid-late 2023."""),
           Arbitrage(target=Stock(ticker_name="IAA", period=period), buyer=Stock(ticker_name="RBA", period=period),
                     offer_price=10, additional_buyer_ratio=0.5804,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - shareholder approval. The current spread largely reflects the risk of IAA
                                shareholder approval (meeting date TBD). Recently, reputable activist Ancore (4% stake)
                                voiced its opposition to the merger, arguing that it undervalues the company. Given the
                                strong strategic rationale and relatively low transaction multiple, there is a decent
                                chance for an improved offer. Both parties seem confident that regulatory approvals will pass.
                                """),
           Arbitrage(target=Stock(ticker_name="HVBC", period=period), buyer=Stock(ticker_name="CZFS", period=period),
                     offer_price=6.1, additional_buyer_ratio=0.32,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - expensive hedging. The key reason for the spread is high borrow fees,
                                currently standing at 13%. Merger is expected to close succesfully by H1'23. Both
                                shareholder and regulatory approval are likely to pass given the larget premium over
                                the historical TBV as wll as the small size of the combined enterprise.
                                """),
           Arbitrage(target=Stock(ticker_name="OIIM", period=period), buyer="Management", offer_price=4.93,
                     additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - Chinese privatization. The spread exists mainly due to the market's
                                skepticism towards anything China-realted. Privatization is led by a reputable PE firm
                                that has carried out similar transactions in the past. Moreover, management is  also
                                particiapating in the buyout that increase the chances of a successful closing.
                                """),
           Arbitrage(target=Stock(ticker_name="SJR", period=period), buyer=Stock(ticker_name="RCI", period=period),
                     offer_price=30.12, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. Regulators have blocked the transaction saying
                                it will significantly dampen competition in Canda (where telecom rates are already
                                among the highest in the world). To alleviate antitrust concerns, the companies have
                                in turn agreed to divest RCI's wireless service division. However, Canada's Competition
                                Committee recently stated that the proposed divestment is not an effective remdey.
                                Anticipated settlement during the attempted mediation has failed. This month, the
                                heaing started a competition Tribunal. Both parties expect to receive regulatory
                                clearance sometime in 2023.
                                """),
           Arbitrage(target=Stock(ticker_name="FCRD", period=period), buyer=Stock(ticker_name="CCAP", period=period),
                     offer_price=1.89,
                     additional_buyer_ratio=0.2063,
                     expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - NAV volatiltiy. This is essentally a NAV for NAV merger with an
                                additional cash portion from buyer's external manager. Final consideration will be
                                determined at the time of closing, which is expected in Q1'23. The spread likely exists
                                due to small capitalization, somewhat confusing consideration calculations, and unknown,
                                but predictable transaction expenses. The main risk is NAV volatility, however, due to
                                short timeline NAV changes are likelty to be minimal.
                                """),
           Arbitrage(target=Stock(ticker_name="ONEM", period=period), buyer=Stock(ticker_name="AMZN", period=period),
                     offer_price=18,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 3, 22, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. Several senators sent a letter to FTC,
                                expressing concerns about Amazon potentially dominating the primary care market as well
                                as acquiring vast amounts of personal data. FTC has already requested additional
                                information from the parties. However, an eventual merger block seems unlikely, given
                                Amazon's limited presence in the primary care market, the highly fragmented nature of
                                the industry, and a negligible One Mediacal market share.
                                """),
           Arbitrage(target=Stock(ticker_name="FORG", period=period), buyer="Thoma Bravo", offer_price=23.25,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - antitrust approval. FORG is getting acquired by PE firm Thoma Bravo.
                                The main risk is regulatory approval due to increased market concentration. Just this
                                year Thomas Bravo has already acquired 2 players in the IAM space - one of which is a
                                direct peer to FORG. Recently, reports came out that Thomas Bravo plans to pull and
                                refile its merger docs with DOJ. Merger is expected to close in the first half of 2023.
                                """),
           Arbitrage(target=Stock(ticker_name="SGFY", period=period), buyer=Stock(ticker_name="CVS", period=period),
                     offer_price=30.5, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 6, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - regulatory approval. The reason for the small spread is still pending
                                regualtory approval. Recently FTC requested additional information due to
                                anti-competitive concerns of the proporsed merger. CSV's managements suggests the deal
                                will pass as both companies provide different products and services. Merger is expected
                                to close in H1'23.
                                """),
           Arbitrage(target=Stock(ticker_name="GSMG", period=period), buyer="Management", offer_price=1.55,
                     additional_buyer_ratio=0, expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - Chinese company and material downside. The price was already raised
                                once from the initial \\$1.27\\/share, which was rejected by the special committee. An
                                improved offer was appoved and a definitive agreement is now in place. Major shareholder
                                US hedge fund Shah Capital is rolling its 11% stake. Shareholder approval has been granted.
                                Downside is very material, which coupled with GSMG being a Chineese company, probably
                                explains the current spread.
                                """),
           Arbitrage(target=Stock(ticker_name="CCHWF", period=period), buyer=Stock(ticker_name="CRLBF", period=period),
                     offer_price=0,
                     additional_buyer_ratio=0.5579, expecting_closing=datetime(2023, 3, 30, tzinfo=timezone.utc),
                     commentary="""**Main risk** - potential dilution to the consideration due to certain earn-out
                                provisions. The merger has already received shareholder approval. Antitrust risks are
                                low. Both parties have recently signed asset divestment as a requiremeent for the merger
                                to close. Other asset divestitues are going as planned. Management expects the merger
                                to close in Q1 2023. The merger exchange ratio is subject to proration adjustment by
                                the amount of Columbia Care shares issued as an earn-out for its historical acqusition
                                form Dec'20. Information on the earn-out would lower the exchange rate to 0.5255 and
                                reduce the spread to 2%.
                                """),
           Arbitrage(target=Stock(ticker_name="SWIR", period=period), buyer=Stock(ticker_name="SMTC", period=period),
                     offer_price=31, additional_buyer_ratio=0,
                     expecting_closing=datetime(2023, 3, 31, tzinfo=timezone.utc),
                     commentary="""The spread used to stand at 2% before widening to the current 7% on the news of the
                                    2nd request from DOJ. \\$SWIR is \\$1.1bn mcap company designing and selling hardware and
                                    services for cellular wireless connectivity, such as 5G. The company produces cellular
                                    wireless routers and gateways (Enterprise Solutions segment) as well as cellular wireless
                                    modules (IoT Solutions). In Aug'22, \\$SWIR agreed to be acquired by semiconductor supplier
                                    \\$SMTC at \\$31/share in cash. The transaction has already been approved by \\$SWIR's
                                    shareholders. The only remaining hurdle is regulatory approval in the US.
                                    Parties expect the merger to close by Mar'23.""")]
    return sorted(res, key=lambda x: x.expecting_closing)
