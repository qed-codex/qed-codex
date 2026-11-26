---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTwistIntersectionAnyDegree.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.TwistIntersectionAnyDegree.proof"
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

## Self-intersection under an embeddingwise constant metric twist

[Theorem ARAK.1575](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.TwistIntersectionAnyDegree.proof/)

Assume the embedding-averaging and generic-degree comparison statements described below. Let $K$ be a nonempty finite set and $I_k$ finite coordinate-index sets, $\Omega$ a field containing a number field $F$, and $y=(y_{k,i})$ a tuple in $\Omega$. Put $$P=\ker\bigl(\mathbb Z[X_{k,i}]\to\Omega[T_k:k\in K],\ X_{k,i}\mapsto y_{k,i}T_k\bigr).$$ Assume $P$ defines an arithmetic variety of dimension $D+1$, $D\ge1$, and every element of $\Omega$ is a ratio of evaluations at $y$ of integral multihomogeneous polynomials of the same multidegree, with nonzero denominator. Let $\overline A,\overline B$ be coordinate line bundles with smooth positive homogeneous metric functions, with multidegree of $B$ equal to zero. For every embedding $\sigma:F\hookrightarrow\mathbb C$, let $\Lambda_\sigma>0$. Assume every complex point of $P$ lies over a unique $\sigma$, and the homogeneous metric function $h_B$ equals the constant $\Lambda_\sigma$ on a neighborhood of every point over $\sigma$.

For any arithmetic intersection system $I$ satisfying symmetry, tensor additivity and divisor recursion on every finite system of coordinate blocks, $$I_X((\overline A\otimes\overline B)^{D+1})=I_X(\overline A^{D+1})+(D+1)\deg_{X_{\mathbb Q}}(A^D)\frac{\sum_{\sigma:F\hookrightarrow\mathbb C}\log\Lambda_\sigma}{[F:\mathbb Q]}.$$ Lying over $\sigma$ means that evaluation of the homogeneous rational functions representing elements of $F$ agrees with $\sigma$.
