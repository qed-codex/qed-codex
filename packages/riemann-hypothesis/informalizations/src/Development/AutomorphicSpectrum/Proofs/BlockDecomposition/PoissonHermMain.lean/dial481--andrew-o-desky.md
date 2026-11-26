---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PoissonHermMain.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.HermPoisson.poissonHerm_main"
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

## Poisson summation for Hermitian Gaussian integrals

[Theorem THETA.1424](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.HermPoisson.poissonHerm_main/)

Assume the source's full arithmetic unitary datum, with CM extension $E/F$. Let $V$ be a Hermitian space in this datum, of rank $n$, and let $r\ge0$ satisfy $2r<n$. Choose a standard adelic additive character $\psi$ of $F$, compatible infinite-place Schwartz data, and $\varphi\in\mathcal S(M_{n,r}(\mathbb A_E))$ in that Schwartz model. Let $\mu$ be additive Haar measure on this matrix space for which the rational lattice has covolume one. Let $\lambda$ be additive Haar measure on the adelic Hermitian matrices $\operatorname{Herm}_r(\mathbb A_E)$ for which $\operatorname{Herm}_r(E)$ has covolume one. Let $\nu$ be Haar measure on $U(V)(\mathbb A_F)$, and assume the associated absolute theta integral is finite.

Write $\langle y,y\rangle_V$ for the $r\times r$ Gram matrix of the columns of $y$, and let $\operatorname{tr}_{E/F}/2$ denote half the field trace, also on adeles. For $b$ an adelic Hermitian matrix define $$J(b)=\int_{M_{n,r}(\mathbb A_E)}\varphi(y)\psi\left(\tfrac12\operatorname{tr}_{E/F}\operatorname{Tr}(b\langle y,y\rangle_V)\right)d\mu(y).$$ For $\beta\in\operatorname{Herm}_r(E)$ put $$W(\beta)=\int_{\operatorname{Herm}_r(\mathbb A_E)}J(b)\psi\left(-\tfrac12\operatorname{tr}_{E/F}\operatorname{Tr}(\beta b)\right)d\lambda(b).$$ If $\sum_{b\in\operatorname{Herm}_r(E)}|J(b)|<\infty$, then $$\sum_{\beta\in\operatorname{Herm}_r(E)}W(\beta)=\sum_{b\in\operatorname{Herm}_r(E)}J(b),$$ where the left-hand side converges as an unordered sum.
