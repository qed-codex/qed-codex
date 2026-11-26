---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/GRPFockOf.lean",
  "declarations": [
    "UpperTheory.TP.RP.fockOf_k"
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

## Archimedean polynomial realization of a Weil representation

[Theorem THETA.1713](https://andrewodesky.com/rh/lean/UpperTheory.TP.RP.fockOf_k/)

Assume the source's full theta-tools package. Let $E$ be a CM number field, $F=E^+$, and choose the base datum $B$ of ([Convergence and polynomial growth of a height Eisenstein sum](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_convergence_bound/)), including the additive character $\psi$ and a complex embedding $\tau_w$ above each infinite place $w$ of $F$. Let $1\le n\le d$, let $X,W$ be Hermitian and skew-Hermitian spaces with the signature and lattice conditions in ([Convergence and polynomial growth of a height Eisenstein sum](https://andrewodesky.com/rh/lean/GlobalTheory.T.eisenstein_series_convergence_bound/)) of dimensions $n,d$, and let $M$ be a Weil model with splitting characters $\chi_X,\chi_W$ and action $\omega$. Assume the complete good-pair conditions of signatures $(n,0),(d,0)$ and compatible topological group identifications from the standard adelic unitary groups to $U(X),U(W)$, preserving rational, infinite, finite and local subgroups and all embedding maps.

Suppose $J_X=1$, $J_W=\delta1$ for some $\delta\in E$, and the archimedean characters are $$\chi_X(z)=\prod_w(z_w/|z_w|)^{m_X(w)},\qquad \chi_W(z)=\prod_w(z_w/|z_w|)^{m_W(w)}$$ for integers $m_X(w),m_W(w)$. Put $\mathcal P=\mathbb C[Z_{ij}:1\le i\le n,1\le j\le d]$ and $\mathcal T=\bigotimes_{w\mid\infty,\mathbb C}\mathcal P$. There is an injective complex-linear map $$\Phi:\mathcal T\longrightarrow\mathcal S\!\left(\prod_{w\mid\infty}M_{n,d}(F_w)\right)$$ whose range is exactly the polynomial subspace of the chosen Weil model, and integer functions $a,b$ with $$2a(w)=d+m_W(w),\qquad2b(w)=n+m_X(w).$$ The infinite components of the two unitary factors act through $\Phi$ by tensor products of $$P(Z)\longmapsto(\det g)^{a(w)}P(g^tZ),\qquad P(Z)\longmapsto(\det h)^{b(w)}P(Zh),$$ respectively, where $g,h$ are their images under $\tau_w$. Equivariance means the adelic Weil action on a pure tensor with any permitted finite factor induces precisely these transformations on its infinite factor.
