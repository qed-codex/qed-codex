---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/BruhatImpliesFieldGeneration.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.EisCovar.FieldGenPf.fieldGen_of_bruhat"
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

## Generators for a split unitary matrix group

[Theorem ALG.0899](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.EisCovar.FieldGenPf.fieldGen_of_bruhat/)

Assume the Siegel Bruhat-decomposition package specified below. Let $K$ be a field of characteristic different from two, let $\sigma:K\to K$ be a ring endomorphism with $\sigma^2=1$, and let $n\ge0$. Put $$J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix},\qquad A^*=\sigma(A)^{\mathsf T},\qquad G=\{g\in\operatorname{GL}_{2n}(K):g^*Jg=J\}.$$ If a multiplicatively closed set of $2n\times2n$ matrices contains $J$, every $$m(a)=\operatorname{diag}(a,(a^*)^{-1})\quad(a\in\operatorname{GL}_n(K)),$$ and every $u(b)=\begin{pmatrix}I_n&b\\0&I_n\end{pmatrix}$ with $b^*=b$, then it contains $G$.
