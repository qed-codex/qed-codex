---
{
  "module": "src/CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/GramFiberMeasureDisintegrationFormulaStatement.lean",
  "declarations": [
    "GlobalTheory.T.gram_fiber_measure_disintegration_formula"
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

## Continuous disintegration over nonsingular Gram matrices

[Theorem ANT.1469](https://andrewodesky.com/rh/lean/GlobalTheory.T.gram_fiber_measure_disintegration_formula/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, and let $J\in M_M(E)$ be a nonsingular $\sigma$-Hermitian matrix. Let $R$ be a reduced Artinian commutative $F$-algebra with a locally compact, second-countable Hausdorff topological-ring structure and its Borel measurable structure. Suppose the inclusion $R^\times\to R$ is an open embedding and there is an open subgroup $U_0\subseteq R^\times$ for which $u\mapsto u^2$ is an open embedding into $R^\times$. Put $V=(R\otimes_FE)^{M\times n}$, let $\mathcal H_n(R)$ be the space of $\sigma$-Hermitian $n\times n$ matrices over $R\otimes_FE$, and let $q:V\to\mathcal H_n(R)$ be the Gram map $q(X)=\sigma(X)^TJX$. Choose additive Haar measures $\mu$ on $V$ and $\nu$ on $\mathcal H_n(R)$.

For every $S\in\mathcal H_n(R)$ whose determinant is a unit, there are an open neighborhood $B\ni S$, consisting of matrices with unit determinant, and measures $\mu_b$ on $V$ for every $b\in\mathcal H_n(R)$. Put $U=q^{-1}(B)$. Each $\mu_b$ is supported on $q^{-1}(b)\cap U$, and for every nonnegative extended-real measurable $f$, $$\int_U f\,d\mu=\int_{\mathcal H_n(R)}\left(\int_Vf\,d\mu_b\right)d\nu(b).$$ For every continuous compactly supported real $f$ with support contained in $U$, $f$ is $\mu_b$-integrable for every $b\in B$, and $b\mapsto\int f\,d\mu_b$ is continuous on $B$.
