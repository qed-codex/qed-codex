---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExactKeyFormulaProof.lean",
  "declarations": [
    "GlobalTheory.KeyFam.keyFormula_holds"
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

## A normalized scalar relating theta sections and Lie bases

[Theorem AV.0039](https://andrewodesky.com/rh/lean/GlobalTheory.KeyFam.keyFormula_holds/)

For a characteristic-zero field $K$, let a datum $x$ consist of an abelian variety $A/K$ of dimension $g\ge1$, a symmetric ample line bundle $L$ with trivial translation kernel, a rigidification of $L$ at zero, a nonzero global section $\theta$, and a basis $v_1,\ldots,v_g$ of $\operatorname{Lie}A$. There is an assignment $\kappa(x)\in K^\times$ with all the following properties.

If $\theta'=a\theta$ and $v'_i=\sum_j M_{ij}v_j$, with the other data fixed, then $$a^8\kappa(x')=(\det M)^4\kappa(x).$$ The assignment commutes with every homomorphism of characteristic-zero fields, when all data, including rigidification, section and Lie basis, are pulled back.

Let $R$ be a discrete valuation domain with characteristic-zero fraction field $K$. If $x$ is defined over $R$, with its theta section nonzero on every fiber, then $\kappa(x_K)$ comes from a unit $u\in R^\times$. For every surjective homomorphism $r:R\to k$ to a characteristic-zero field, the corresponding base-changed datum satisfies $\kappa(x_k)=r(u)$.

Over $\mathbb C$, let $A(\mathbb C)=\mathbb C^g/\Lambda$ with a holomorphic trivialization of the pulled-back line bundle compatible with the rigidification. If $\Lambda=\mathbb Z^g+\tau\mathbb Z^g$, where $\tau$ is symmetric with positive-definite imaginary part, the section is the theta function $$\theta[a,b](z,\tau)=\sum_{n\in\mathbb Z^g}e^{\pi i(n+a)^t\tau(n+a)+2\pi i(n+a)^t(z+b)},$$ with $a_i,b_i\in\{0,\tfrac12\}$, and $v_i$ corresponds to $(2\pi i)^{-1}$ times the $i$-th coordinate vector, then $\kappa(x)=1$.

More generally, suppose the section is represented by $\vartheta(z)$ and the trivialization has factors $$f(z)=\chi(l)e^{\pi z^tH\bar l+\pi l^tH\bar l/2}f(z+l)\qquad(l\in\Lambda),$$ where $H$ is positive-definite Hermitian and $|\chi(l)|=1$. If the rows of $W$ represent $v_i$, $D$ is an additive fundamental domain of $\Lambda$, and $$N_\theta=\frac{1}{\operatorname{vol}D}\int_D|\vartheta(z)|^2e^{-\pi\operatorname{Re}(z^tH\bar z)}\,dz,\qquad N_\eta=\frac{\operatorname{vol}D}{\pi^g|\det W|^2},$$ then $|\kappa(x)|N_\theta^4N_\eta^2=(2\pi)^{2g}$.
