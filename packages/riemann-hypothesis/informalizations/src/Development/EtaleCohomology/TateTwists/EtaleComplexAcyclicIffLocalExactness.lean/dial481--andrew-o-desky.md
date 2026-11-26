---
{
  "module": "src/Development/EtaleCohomology/TateTwists/EtaleComplexAcyclicIffLocalExactness.lean",
  "declarations": [
    "LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_acyclic_cone_of_flat",
    "LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_acyclic_of_staircase_lifting"
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

## Local acyclicity of a bounded-below tensor total complex

[Theorem AG.0987](https://andrewodesky.com/rh/lean/LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_acyclic_of_staircase_lifting/)

Let $R$ be a commutative ring, and let $C,J,T$ be cochain complexes of sheaves of $R$-modules on the big étale site of schemes. Suppose $C^s=0$ for $s<a$ and $J^t=0$ for $t<b$, where $a,b\in\mathbb Z$, and fix a tensor pairing identifying $T$ with the tensor total complex of $C$ and $J$.

Assume each column $C\otimes_RJ^t$ is locally exact in the following explicit sense: whenever $U$ is a scheme and $$x\in C^s(U)\otimes_RJ^t(U),\qquad(d_C\otimes1)x=0,$$ there is an étale covering $(U_\alpha\to U)$ and elements $$y_\alpha\in C^{s-1}(U_\alpha)\otimes_RJ^t(U_\alpha),\qquad(d_C\otimes1)y_\alpha=x|_{U_\alpha}.$$ Then $T$ is locally acyclic: every section in the kernel of $d_T:T^n\to T^{n+1}$ is, after an étale covering, in the image of $d_T:T^{n-1}\to T^n$.

## A flat bounded-below etale tensor factor preserves acyclicity

[Theorem AG.1007](https://andrewodesky.com/rh/lean/LateralTheory.Fin.EtaleTensorPairQuasiIsoOfFlatQuasiIso.etale_tensor_acyclic_cone_of_flat/)

Let $R$ be a commutative ring, and let $C,J$ be cochain complexes of sheaves of $R$-modules on the big étale site of schemes. Suppose $C$ and $J$ vanish below integers $a$ and $b$, respectively, every sheaf $J^t$ satisfies the flatness condition below, and $C$ is acyclic. Then the total tensor complex $\operatorname{Tot}(C\otimes_RJ)$ is acyclic.
