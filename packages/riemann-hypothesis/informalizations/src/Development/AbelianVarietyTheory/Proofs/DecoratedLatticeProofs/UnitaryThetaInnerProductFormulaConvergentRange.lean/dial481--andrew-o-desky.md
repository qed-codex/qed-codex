---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UnitaryThetaInnerProductFormulaConvergentRange.lean",
  "declarations": [
    "GlobalTheory.Core.Rk.IP.innerProduct_convergent"
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

## The theta inner-product identity in the convergent range

[Theorem THETA.1004](https://andrewodesky.com/rh/lean/GlobalTheory.Core.Rk.IP.innerProduct_convergent/)

Assume the three universal analytic inputs below, and work in the source's full arithmetic unitary datum over a CM extension $E/F$. Let $A,B$ be Hermitian spaces with $\dim_EA=n\ge1$, $\dim_EB=n+t$, $t\ge1$, and $$n<t,\qquad \operatorname{Witt}(B)=0\ \text{or}\ \operatorname{Witt}(B)<t.$$ Fix a compatible theta datum: an adelic additive character $\psi$, archimedean embeddings and Cartan involutions, splitting characters $\chi_A,\chi_B$, a Weil representation $\omega$ for $U(A)\times U(B)$, and a covolume-one fundamental domain $\mathcal F$ for the rational subgroup of its adelic Heisenberg parameter space $W$. Choose a signature-compatible compact frame for $A$ and a majorant frame taking its positive Cartan form to the identity.

Let $m,m_B$ be any Haar measures on $G_A=U(A)(\mathbb A_F)$ and $G_B=U(B)(\mathbb A_F)$. For polynomial Fock theta vectors $\Phi_1,\Phi_2$ in the specified Cartan models and smooth compact-finite cusp forms $u_1,u_2$ on $G_A$, put $$\Theta(\Phi,u)(h)=\int_{[G_A]}\theta_\omega(g,h;\Phi)u(g)\,d\bar m(g),$$ $$c_\omega(g)=\int_{\mathcal F}(\omega(g,1)\Phi_1)(w)\overline{\Phi_2(w)}\,d\nu(w),\qquad c_u(g)=\langle R_gu_1,u_2\rangle_{[G_A]}.$$ Both theta-lift integrals converge absolutely at every $h$, both lifts belong to $L^2([G_B])$, $c_\omega c_u\in L^1(G_A,m)$, and $$\langle\Theta(\Phi_1,u_1),\Theta(\Phi_2,u_2)\rangle_{[G_B]}=\operatorname{vol}([G_B])\int_{G_A}c_\omega(g)c_u(g)\,dm(g).$$
