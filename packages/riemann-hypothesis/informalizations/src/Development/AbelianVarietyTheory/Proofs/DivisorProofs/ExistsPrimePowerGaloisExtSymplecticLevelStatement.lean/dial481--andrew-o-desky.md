---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsPrimePowerGaloisExtSymplecticLevelStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_primePower_galois_ext_symplecticLevel"
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

## A symplectic level structure after a prime power Galois extension

[Theorem AV.1102](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_primePower_galois_ext_symplecticLevel/)

Let $\Omega_1$ be a field of characteristic zero, $R_1$ a commutative ring with a homomorphism $R_1\to\Omega_1$, and $(A,L)$ a polarized abelian scheme of dimension $g$ over $R_1$. Let $\ell$ be prime, $M>0$ with $\ell\mid M$, and $K=\ell^e$ for some $e\ge0$. Suppose $\Omega_1$ contains a primitive $M$-th root of unity, and every geometric $M$-torsion point of $A$ is the specialization of a section of $A/R_1$.

There is a finite Galois extension $\Omega_2/\Omega_1$ of degree a power of $\ell$, a primitive $K$-th root of unity $\zeta\in\Omega_2^\times$, and a polarized abelian variety $(Q,L_Q)/\Omega_2$ of dimension $g$ obtained by base change from $(A,L)$, with $L_Q\simeq L|_Q$, such that $Q$ has a full symplectic level-$K$ structure with respect to $\zeta$.
