---
{
  "module": "src/Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/LogBallEstimates.lean",
  "declarations": [
    "PositivityTheory.AdelicQuotientData.duality_diagonalClass_of_affineProperBaseChange"
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

## Holomorphic regularization of an adelic Mellin integral

[Theorem ANT.1631](https://andrewodesky.com/rh/lean/PositivityTheory.AdelicQuotientData.duality_diagonalClass_of_affineProperBaseChange/)

Assume the source's determinant-norm identities, quotient-measure invariance and power integrability, and split-central band-integral formula. Let $E$ be totally complex, $k\ge1$, $G=\operatorname{GL}_k(\mathbb A_E)$, and $D(g)>0$ its adelic determinant norm. Let $\mu$ be the source's Haar measure, let $\beta$ be a quotient weight for the specified rational integration measure, and put $d\nu=\beta\,d\mu$. Put $\mathcal B=\{g:1\le D(g)<\exp(k[E:\mathbb Q])\}$. Let $H,H_0$ be measurable, left $\operatorname{GL}_k(E)$-invariant complex functions, with $H_0$ bounded and invariant under the real split centre. Assume that for every $M\ge0$ there is $C_M\in\mathbb R$ with $|H(g)|\le C_MD(g)^{-M}$ when $D(g)\ge1$, and that some $C\in\mathbb R$ satisfies $|D(g)H(g)-H_0(g)|\le CD(g)$ when $D(g)<1$.

There is a holomorphic function $Z$ on $\Re s>0$ with $$Z(s)=(s-1)\int_G H(g)D(g)^s\,d\nu(g)\qquad(\Re s>1).$$ Furthermore, $$\int_{\mathcal B}H_0(g)\,d\nu(g)=0\quad\Longrightarrow\quad Z(1)=0.$$
