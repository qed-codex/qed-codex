---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/FockVectorsInnerEqFockInnerProductMulNormStatement.lean",
  "declarations": [
    "GlobalTheory.T.fockVectors_inner_eq_fockInnerProduct_mul_norm"
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

## The polynomial pairing of adelic Fock vectors

[Theorem THETA.0781](https://andrewodesky.com/rh/lean/GlobalTheory.T.fockVectors_inner_eq_fockInnerProduct_mul_norm/)

Use the arithmetic datum of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) and Hermitian spaces $S,T$ in ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)). Choose an additive character $\psi$ and compatible archimedean maps $\theta$ with the normalization specified in ([Weil actions and prescribed theta test vectors](https://andrewodesky.com/rh/lean/Formalism.IndefR.WeilFull.IsWeilFull/)). At each infinite place $\tau$, choose Cartan involutions $s_{S,\tau},s_{T,\tau}$ and signed orthonormal bases $B_{S,\tau},B_{T,\tau}$ with positive indices $p_{S,\tau}\le\dim S$, $p_{T,\tau}\le\dim T$, satisfying the identities below. Let $f$ be a theta function annihilated by every archimedean annihilation operator for these Cartan involutions.

Let $\mu$ be an additive Haar measure on the adelic matrix space $\operatorname{Hom}_E(S,T)\otimes_F\mathbb A_F$, and $\mathcal F$ a fundamental domain for its rational matrix lattice with $\mu(\mathcal F)=1$. Write $\mathcal P(P)=P(a^+)f$ for the normalized polynomial Fock vector. For every pair of polynomials $P,Q$, $$\int_{\mathcal F}\mathcal P(P)(w)\overline{\mathcal P(Q)(w)}\,d\mu(w) =\left(\sum_\alpha\alpha!\,P_\alpha\overline{Q_\alpha}\right)\int_{\mathcal F}|f(w)|^2\,d\mu(w).$$
