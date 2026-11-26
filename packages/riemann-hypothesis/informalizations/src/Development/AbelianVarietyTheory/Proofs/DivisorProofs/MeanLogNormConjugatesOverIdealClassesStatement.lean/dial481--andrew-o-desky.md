---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/MeanLogNormConjugatesOverIdealClassesStatement.lean",
  "declarations": [
    "GlobalTheory.T.mean_log_norm_conjugates_over_ideal_classes"
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

## A logarithmic norm bound from equally distributed ideal classes

[Theorem ANT.1136](https://andrewodesky.com/rh/lean/GlobalTheory.T.mean_log_norm_conjugates_over_ideal_classes/)

Let $K$ be an imaginary quadratic field with embedding $\iota:K\hookrightarrow\mathbb C$, class group $C$ and class number $h$. Put $G=\operatorname{Aut}(\mathbb C/\iota(K))$. Choose an algebraic $j_0\in\mathbb C$ and nonzero invertible fractional ideals $\mathfrak a_\sigma$ of $K$ for every $\sigma\in\operatorname{Aut}(\mathbb C)$. Assume that, for $\sigma,\sigma'\in G$, $$[\mathfrak a_\sigma]=[\mathfrak a_{\sigma'}]\ \Longleftrightarrow\ \sigma(j_0)=\sigma'(j_0).$$ For every finite Galois subfield $M\subset\mathbb C$ containing $\iota(K)$ and $j_0$, assume each $c\in C$ occurs for exactly $[M:\mathbb Q]/(2h)$ embeddings $\tau:M\hookrightarrow\mathbb C$ which are restrictions $\tau=\sigma|_M$ of some $\sigma\in G$ with $[\mathfrak a_\sigma]=c$. Let $\beta\ne0$ be algebraic over $\mathbb Q$ and let $F:\operatorname{Aut}(\mathbb C)\to\mathbb R$ be constant on ideal classes within $G$, with $\log|\sigma(\beta)|\le F(\sigma)$ for $\sigma\in G$. There are representatives $\sigma_c\in G$ with $[\mathfrak a_{\sigma_c}]=c$ and $$\log|m_\beta(0)|\le\frac{\deg m_\beta}{h}\sum_{c\in C}F(\sigma_c),$$ where $m_\beta\in\mathbb Q[T]$ is the monic minimal polynomial of $\beta$.
