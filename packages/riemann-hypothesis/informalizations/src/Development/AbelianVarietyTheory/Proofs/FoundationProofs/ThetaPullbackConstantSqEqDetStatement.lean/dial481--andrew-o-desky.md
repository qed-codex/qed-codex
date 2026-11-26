---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/ThetaPullbackConstantSqEqDetStatement.lean",
  "declarations": [
    "GlobalTheory.T.thetaPullbackConstant_sq_eq_det"
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

## A theta pullback scalar and a determinant up to a root of unity

[Theorem THETA.0673](https://andrewodesky.com/rh/lean/GlobalTheory.T.thetaPullbackConstant_sq_eq_det/)

Fix the source's global arithmetic CM datum, with its imaginary quadratic field $K$, CM extension field $E$, distinguished integer $d$, embedding $\phi_0:K\hookrightarrow\mathbb C$, and chosen embeddings $\tau:E\hookrightarrow\mathbb C$. Let $\mathfrak c\subseteq\mathcal O_K$ be a nonzero ideal with $\gcd(N\mathfrak c,2d)=1$, and let $$\delta^{12}=\Delta(\phi_0(\mathfrak c)),\qquad\Lambda=\delta\phi_0(\mathfrak c).$$ Fix $t_0\in\mathbb C$ such that $$2t_0\in\Lambda,\qquad \frac{1\pm i\sqrt d}{2}t_0\notin\Lambda.$$ For $N,N',r\ge0$, give $M_{N'\times N}(E)$ the $K$-Hermitian form $$h(A,B)=\operatorname{Tr}_{E/K}\sum_{i,j}A_{ij}\overline{B_{ij}}.$$ Let $(b_j)_{j=1}^r$ and $(b'_j)_{j=1}^r$ be $K$-spanning orthonormal families for $h$. Let $F_b,F_{b'}$ and $\mathcal I$ have the normalizations below. There are $c,\zeta\in\mathbb C$ and $m\ge1$ such that $$\zeta^m=1,\qquad c^2=\zeta\,\phi_0\!\left(\det(h(b'_j,b_i))_{i,j=1}^r\right),\qquad F_{b'}=c\,\mathcal I_{\Lambda_b,\Lambda_{b'}}F_b.$$
