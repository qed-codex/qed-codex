---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianSpacesSameSignatureIsometricStatement.lean",
  "declarations": [
    "GlobalTheory.T.hermitian_spaces_same_signature_isometric"
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

## Self-dual Hermitian spaces with equal signatures are isometric

[Theorem ANT.0577](https://andrewodesky.com/rh/lean/GlobalTheory.T.hermitian_spaces_same_signature_isometric/)

Let $E$ be a totally complex number field with a ring involution $a\mapsto\bar a$ inducing complex conjugation under every embedding $E\hookrightarrow\mathbb C$. Assume that for every maximal ideal $\mathfrak p\subseteq\mathcal O_E$, there is $\theta\in\mathcal O_E$ with $\theta-\bar\theta\notin\mathfrak p$. Let $J,J'\in M_n(E)$ be nonsingular Hermitian matrices. Assume each form admits a full self-dual $\mathcal O_E$-lattice: for each $H\in\{J,J'\}$ there is a full lattice $\Lambda_H\subseteq E^n$ with $$\Lambda_H=\{x\in E^n:\bar y^{\,t}Hx\in\mathcal O_E\text{ for every }y\in\Lambda_H\}.$$ Suppose $\phi(J)$ and $\phi(J')$ have the same signature for every embedding $\phi:E\hookrightarrow\mathbb C$. Then there is $\gamma\in\operatorname{GL}_n(E)$ with $$\bar\gamma^{\,t}J\gamma=J'.$$

**Positive definite spaces in arithmetic families.** Choose an arithmetic datum satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), with CM field $E$ and conjugation $c$. Let $W$ be a Hermitian space of rank $r\ge0$ with recorded lattice data in the generic definition of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), equipped with assigned signatures at the embeddings, each equal to the signature of its Hermitian matrix at that embedding. If its signature at every complex embedding of $E$ is $(r,0)$, there are $E$-linearly independent vectors $b_1,\ldots,b_r\in W$ such that $$h(b_i,b_j)=\delta_{ij}.$$
