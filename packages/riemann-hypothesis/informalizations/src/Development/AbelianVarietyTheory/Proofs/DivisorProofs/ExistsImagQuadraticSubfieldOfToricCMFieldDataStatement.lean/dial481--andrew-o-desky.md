---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsImagQuadraticSubfieldOfToricCMFieldDataStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_imagQuadratic_subfield_of_toricCMFieldData"
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

## A common imaginary quadratic subfield for a CM type

[Theorem ANT.1277](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_imagQuadratic_subfield_of_toricCMFieldData/)

Let $E$ be a number field, $I$ a finite set, $d$ a prime with $d>4$ and $d\equiv3\pmod4$, and $\varphi_i:E\hookrightarrow\mathbb C$ for $i\in I$. Let $E^+$ be the maximal real subfield. Assume $$\mathfrak D_{\mathcal O_E/\mathcal O_{E^+}}=\mathcal O_E,\qquad 2\mid\operatorname{disc}E,\qquad |I|\ge2.$$ Suppose that every embedding $\sigma:E\hookrightarrow\mathbb C$ equals $\varphi_i$ or $\overline{\varphi_i}$ for exactly one $i$, that $\prod_i\varphi_i(u)=1$ for every finite-order $u\in E$, and that there is $w\in E$ with $$w^2=-d,\qquad \varphi_i(w)=\mathrm i\sqrt d\quad(i\in I).$$ Let $\Lambda\subseteq\mathbb C$ be a period lattice satisfying $$\Lambda=\{z\in\mathbb Q+\mathbb Q\,\mathrm i\sqrt d:z\text{ is integral over }\mathbb Z\}.$$ There are an intermediate field $\mathbb Q\subseteq K\subseteq E$ and an embedding $\varphi_K:K\hookrightarrow\mathbb C$ such that $$[K:\mathbb Q]=2,\qquad\operatorname{disc}K=-d,\qquad\varphi_i|_K=\varphi_K\ (i\in I),\qquad\overline{\varphi_K}\ne\varphi_K,\qquad \Lambda=\varphi_K(\mathcal O_K).$$
