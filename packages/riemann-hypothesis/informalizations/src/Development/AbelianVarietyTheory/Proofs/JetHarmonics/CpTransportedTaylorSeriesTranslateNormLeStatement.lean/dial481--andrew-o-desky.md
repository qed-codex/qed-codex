---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/CpTransportedTaylorSeriesTranslateNormLeStatement.lean",
  "declarations": [
    "GlobalTheory.T.cpTransportedTaylorSeries_translate_norm_le"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## A coefficient bound preserved by elliptic translation

[Theorem PHT.0860](https://andrewodesky.com/rh/lean/GlobalTheory.T.cpTransportedTaylorSeries_translate_norm_le/)

Let $q$ be prime, write $\mathbb C_q$ for the completed algebraic closure of $\mathbb Q_q$, and let $\iota:\mathbb C\simeq\mathbb C_q$ be a field isomorphism. Let $\Lambda$ be a complex period lattice with Weierstrass invariants $g_2,g_3$. Choose $c\in\mathbb C^\times$ and a Weierstrass curve $W/\mathbb C_q$ with $$|a_i(W)|_q\le1\ (i=1,2,3,4,6),\qquad |\Delta_W|_q=1,$$ $$c_4(W)/12=\iota(g_2/c^4),\qquad c_6(W)/216=\iota(g_3/c^6).$$ Define $x,y,u$ and $\widehat f$ in the conventions. Let $\ell\in\mathbb C_q[[T]]$ have zero constant term, assume every coefficient of $\widehat u$ has norm at most one, and assume $|[T]\widehat u|_q=1$.

Let $t\in\mathbb C$ and let $\varphi:\mathbb C\to\mathbb C$ be meromorphic and $\Lambda$-periodic, analytic at $0$ and $t$. Suppose every pole $z$ of $\varphi$ satisfies $$z\notin\Lambda,\qquad |\iota(x(z))|_q\le1,$$ and suppose the same two conditions hold for $t$. If the coefficients of $\widehat{\varphi(\,\cdot+t)}$ are bounded and those of $\widehat\varphi$ have norm at most $B\in\mathbb R$, then every coefficient of $\widehat{\varphi(\,\cdot+t)}$ also has norm at most $B$.
