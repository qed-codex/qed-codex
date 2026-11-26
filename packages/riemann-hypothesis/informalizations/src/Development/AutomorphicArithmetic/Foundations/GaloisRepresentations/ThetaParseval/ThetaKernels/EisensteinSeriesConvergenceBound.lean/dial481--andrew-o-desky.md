---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/EisensteinSeriesConvergenceBound.lean",
  "declarations": [
    "GlobalTheory.T.eisenstein_series_convergence_bound"
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

## Convergence and polynomial growth of a height Eisenstein sum

[Theorem ANT.1308](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_convergence_bound/)

Let $E/F$ be number fields with an $F$-automorphism $\sigma$, supplied with the following base datum: an additive character $\psi$ of $\mathbb A_F$, choices of infinite embeddings, and finite-place embeddings. Assume the full base conditions: $E/F$ is a CM extension with conjugation $\sigma$; $E$ contains an element with square $-d$ for some positive integer $d$; $\mathcal O_E/\mathcal O_F$ is unramified; $\psi$ is continuous and trivial on $F$, and on pure archimedean adeles $a$ it equals $\exp(-2\pi i\operatorname{Tr}_{F_\infty/\mathbb R}a)$; at the selected finite places and at every inert place its local component satisfies $\{x:\psi_v(x\mathcal O_{F_v})=1\}=\mathcal O_{F_v}$; and every inert residue characteristic is odd and has residue cardinality greater than three.

Let $Y$ have rank $n\ge1$ and satisfy the source's Hermitian or skew-Hermitian lattice package for some signatures $(r,s)$. Form the doubled unitary group $G=U(Y\oplus(-Y))$. Choose a hyperbolic frame compatible with its diagonal isotropic subspace, and the corresponding standard compact subgroup $K\subset G(\mathbb A_F)$. Let $P$ stabilize that isotropic subspace. Suppose every $x\in G(\mathbb A_F)$ can be written $x=pk$ with $p\in P(\mathbb A_F)$, $k\in K$, and let $a$ be the function characterized by $$a(pk)=|\det(t)|_{\mathbb A_E},$$ where $t$ is the action of $p$ on the diagonal isotropic subspace. Let $H(x)=\prod_u\max(1,\|x_u\|_u,\|x_u^{-1}\|_u)$, where $u$ ranges over places of $F$; at a finite place the matrix norm is the maximum absolute value of an entry over all embeddings of $E$ above $u$, and at an infinite place it is the maximum Euclidean operator norm over those embeddings.

There is $\sigma_0\in\mathbb R$ such that for every real $\sigma'>\sigma_0$ there are $C\in\mathbb R$ and an integer $N\ge0$ with, for every $x$, $$\sum_{\gamma\in P(F)\backslash G(F)}a(\gamma x)^{\sigma'}\le C H(x)^N,$$ and the sum converges as an unordered sum, using one fixed representative for each rational parabolic coset.
