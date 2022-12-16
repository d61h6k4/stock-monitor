from stock_monitor.models import Stock, Arbitrage
from datetime import datetime, timezone
from streamlit import cache


def tickers():
    return ["GOOG", "NVDA", "ASML", "KLAC", "PBR", "TGNA", "FSTX", "KOP", "CEG"]


@cache(persist=False, ttl=3600, allow_output_mutation=True)
def stocks(period: str):
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
        res.append(Stock(ticker_name, period=period, buy_date=buy_date))
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
                     expecting_closing=datetime(2022, 12, 31, tzinfo=timezone.utc),
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
                     expecting_closing=datetime(2022, 12, 19, tzinfo=timezone.utc),
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
           Arbitrage(target=Stock(ticker_name="LOTZ", period=period), buyer=Stock(ticker_name="SFT", period=period),
                     offer_price=0, additional_buyer_ratio=0.69,
                     expecting_closing=datetime(2022, 12, 22, tzinfo=timezone.utc),
                     commentary="""**Main risk** - expensive hedging. The merger is basically an equity raise for the
                                buyer, however, the combination will also allow SFT to enter East Cost markets.
                                Shareholder approvals shouldn't be a problem as two major shareholders of LOTZ (25%)
                                are in support. THe main issue is hedging - borrow fees are volatile and quite high at
                                nearly 15%. There is also a minimum net cash condition, but it shouldn't be a problem
                                if the merger closes with no delays.
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
                     additional_buyer_ratio=0, expecting_closing=datetime(2022, 12, 22, tzinfo=timezone.utc),
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
