---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LatDictZPlane.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.LatDictZ.Z2.primitive_plane_local"
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

## An integral partner of prescribed norm for a primitive vector

[Theorem ALG.0214](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.LatDictZ.Z2.primitive_plane_local/)

Let $K$ be a totally complex number field with conjugation $*$, satisfying $\tau(x^*)=\overline{\tau(x)}$ for every complex embedding. Suppose that at every maximal ideal $\mathfrak q\subset\mathcal O_K$ there is $\theta\in\mathcal O_K$ with $\theta-\theta^*\notin\mathfrak q$. Let $V$ be a finite-dimensional $K$-space with a nondegenerate Hermitian form $h$, conjugate-linear in the first variable. Fix a maximal ideal $\mathfrak p$ and put $O=(\mathcal O_K)_{\mathfrak p}\subset K$.

Let $N\subset V$ be an additive subgroup stable under $O$, with $h(N,N)\subset O$, satisfying $$\{x\in V:h(N,x)\subset O\}=N,$$ and suppose every vector in $V$ becomes an element of $N$ after multiplication by some nonzero element of $K$. Let $z\in N$ satisfy $$cz\in N\Longrightarrow c\in O\quad(c\in K),$$ and assume $h(z,z)$ is not a unit in $O$. Let $b\in O$ with $b^*=b$. If there is $w\in V$ with $h(z,w)=1$ and $h(w,w)=b$, there is such a vector $y\in N$.
