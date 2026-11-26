---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SemisimpleOfInjective.lean",
  "declarations": [
    "GlobalTheory.BlockComplement.exists_complement"
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

## An integral complement to specified character summands

[Theorem REP.0649](https://andrewodesky.com/rh/lean/GlobalTheory.BlockComplement.exists_complement/)

Let $O$ be a principal ideal domain with a ring topology, $K=\operatorname{Frac}O$, and let $\Gamma$ be a group with a topology. Let $L$ be a characteristic-zero field and $\varphi:K\hookrightarrow L$ a field embedding. Fix $n=a+t$, a homomorphism $r:\Gamma\to\operatorname{GL}_n(O)$ whose matrix-entry map is continuous and whose extension to $K$ is semisimple, and characters $\chi_j:\Gamma\to O^\times$ for $j\ge0$.

Suppose $T:\Gamma\to L$ is the character of a finite-dimensional $L$-representation and $$\varphi(\operatorname{tr}r(g))=T(g)+\sum_{j=1}^{t}\varphi(\chi_j(g))\qquad(g\in\Gamma).$$ There is a homomorphism $\rho:\Gamma\to\operatorname{GL}_a(O)$ with continuous matrix-entry map such that $$r_K\simeq\rho_K\oplus\bigoplus_{j=1}^{t}\chi_j.$$ The representation on the right is semisimple.

**Polynomial formulation.**

Let $\Gamma$ be a compact topological group, $O$ a discrete valuation ring with a ring topology, and $K$ its characteristic-zero fraction field. Let $r,t\ge0$, let $\rho:\Gamma\to\operatorname{GL}_{r+t}(O)$ have continuous matrix entries, and let $\chi_1,\ldots,\chi_t:\Gamma\to O^\times$ be characters. Suppose $\rho_K$ is semisimple. Assume there exist a field $L$, an embedding $f:K\hookrightarrow L$, and $\rho_0:\Gamma\to\operatorname{GL}_r(L)$ with $$f\bigl(\det(X-\rho(g))\bigr)=\det(X-\rho_0(g))\prod_{i=1}^t(X-f(\chi_i(g)))\qquad(g\in\Gamma),$$ where $f$ acts on the coefficients and the inclusion $O\subseteq K$ is understood. Then there is $\rho':\Gamma\to\operatorname{GL}_r(O)$ with continuous matrix entries and semisimple generic fibre such that $$\det(X-\rho(g))=\det(X-\rho'(g))\prod_{i=1}^t(X-\chi_i(g))\qquad(g\in\Gamma).$$
