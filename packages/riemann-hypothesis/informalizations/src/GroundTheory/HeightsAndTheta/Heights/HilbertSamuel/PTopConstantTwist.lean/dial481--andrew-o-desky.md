---
{
  "module": "src/GroundTheory/HeightsAndTheta/Heights/HilbertSamuel/PTopConstantTwist.lean",
  "declarations": [
    "GroundTheory.Heights₂.Heights.HilbertSamuel.TopConstantTwist.proof"
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

## Change of top arithmetic intersection under a constant metric twist

[Theorem ARAK.1526](https://andrewodesky.com/rh/lean/GroundTheory.Heights%E2%82%82.Heights.HilbertSamuel.TopConstantTwist.proof/)

Let $\{I_k\}_{k\in K}$ be finitely many finite coordinate blocks and let $P\subseteq\mathbb Z[X_{k,i}]$ define an arithmetic variety of relative dimension $D\ge0$ in the multihomogeneous formulation specified in the conventions. Let $\overline L$ be a line bundle given by an integral multidegree and a smooth positive homogeneous metric function $h$. Let $I$ be an arithmetic intersection system satisfying the symmetry, tensor-additivity and divisor-recursion axioms in ([Arithmetic intersection and volume](https://andrewodesky.com/rh/lean/PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright/)). For $c\in\mathbb R$, write $\overline L(c)$ for the same multidegree with homogeneous metric function $e^{-c}h$. Then $$I_X\bigl(\overline L(c)^{D+1}\bigr) =I_X\bigl(\overline L^{D+1}\bigr)-(D+1)c\,\deg_X(L^D),$$ where $\deg_X(L^D)$ is the source's geometric multidegree.
