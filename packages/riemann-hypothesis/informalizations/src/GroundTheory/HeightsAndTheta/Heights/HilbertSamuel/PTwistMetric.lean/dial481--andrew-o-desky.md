---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTwistMetric.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.TwistMetric.proof"
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

## Zero-mean archimedean metric changes with a small intersection cost

[Theorem ARAK.1644](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.TwistMetric.proof/)

Assume the embedding-weight construction specified in the conventions and ([Self-intersection under an embeddingwise constant metric twist](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.TwistIntersectionAnyDegree.proof/)) in every degree. Let $K$ be a finite nonempty set of blocks with finite variable sets $I_k$, let $F$ be a number field embedded in a field $\Omega$, and let $y_{k,i}\in\Omega$. Write $P$ for the ideal of multihomogeneous integral relations of $y$ and assume it is a relevant multihomogeneous prime with $P\cap\mathbb Z=0$ and $\dim(\mathbb Z[X_{k,i}]/P)=D+1+|K|$, where $D\ge1$, and every element of $\Omega$ is a ratio $g(y)/h(y)$ of integral multihomogeneous polynomials $g,h$ of the same multidegree with $h(y)\ne0$. Here relevant means that every block has a variable outside $P$. Fix an arithmetic intersection system $\mathcal I$ satisfying the symmetry, tensor additivity and divisor recursion conditions of ([Self-intersection under an embeddingwise constant metric twist](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.TwistIntersectionAnyDegree.proof/)), an ideal $P_0\subseteq P$, and a Hermitian line datum $A=(a,h)$, with multidegree $a\in\mathbb Z^K$ and positive homogeneous metric function $h$.

Assume $h$ is smooth and conjugation invariant, and the Levi form of $\log h$ is nonnegative on the tangent cone cut out by $P_0$ at every complex point of $P$. Assume every such complex coordinate point lies over a unique embedding $\sigma:F\hookrightarrow\mathbb C$. Let $u_\sigma\in\mathbb R$ satisfy $u_{\bar\sigma}=u_\sigma$ and $\sum_\sigma u_\sigma=0$. There is $C\in\mathbb R$ such that, for every $\delta>0$, there is $A'=(a,h')$ with the same smoothness, conjugation invariance and relative semipositivity, satisfying $$h'(z)=e^{u_\sigma+\delta}h(z)\quad\text{when }z\text{ lies over }\sigma,$$ $$\mathcal I_P(\underbrace{A',\ldots,A'}_{D+1})\le\mathcal I_P(\underbrace{A,\ldots,A}_{D+1})+C\delta.$$
