---
{
  "module": "src/Formalism/SharpRestriction/CuspSpanNormBounds/LocalBesselAndTopKernel.lean",
  "declarations": [
    "Formalism.MainNotions.LocalBesselAndTopKernel.FamilyMidVolume"
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

## Normalized Gram operators and the standing conditions of the diagonal estimate

[Definition / hypothesis THETA.D257](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Kmat/)

Let $D$ be a datum in the sense of ([Datum of the construction and objects over it](https://andrewodesky.com/rh/lean/GlobalTheory.EX.OB.Obj/)). This page defines, for every source $z$ of $D$, an endomorphism $K_z$ of a finite-dimensional Hilbert space, and it lists the conditions on $D$ under which the diagonal estimate bounds the Hilbert–Schmidt distance from $K_z$ to the identity.

**Notation.** The following components of $D$ are used, with the names of the pages that introduce them.

- From ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)): the CM field $E$ and its maximal totally real subfield $F$; the degree $f=[F:\mathbb Q]$; the even integers $k$ and $m$, which satisfy $2\le m$ and $m+3\le k$; the integers $r=k+m-1$ and $r_S=m/2-1$; the root discriminant $\operatorname{rd}_E$; and the distinct primes $g_0,g_1$.
- From ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)): the finite nonempty set $\mathcal W$ of sources; the index set $\mathcal T$ of cardinality $f$, identified with the CM type of $E$; for every source $z$ and every $\tau\in\mathcal T$, the first row $U^z_\tau=(U^z_{\tau,i})_{0\le i<k}$ of the weight array of ([Interlacing weight arrays](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.HCParam/)); for every source $z$, the prime $T_z$, the positive integer $d^*_z$ and the space $U^0_z$ of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)); the positive real numbers $d_\tau$ for $\tau\in\mathcal T$; and the positive real number $D_*$.
- From ([Moment data for the family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)): the finite-dimensional complex inner-product spaces $H_{\rm mom}$ and $C_z$; the complex-linear maps $P_z:C_z\to H_{\rm mom}$; and the positive real numbers $v_N(z)$, $v_H(z)$.

The datum contains a linear isomorphism $C_z\simeq U^0_z$ for every source $z$. Put $$d_z=\dim_{\mathbb C}C_z=\dim_{\mathbb C}U^0_z .$$ The sources are the source words of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)), and $d_z$, $T_z$, $U^z_\tau$ are the quantities written $d_u$, $T_u$, $U^u_\tau$ there.

**The normalized Gram operator.** Let $\rho=\bigl(\tfrac{k-1}{2}-i\bigr)_{0\le i<k}$. For a source $z$ and $\tau\in\mathcal T$, let $\pi_{z,\tau}$ be the irreducible unitary representation of the compact unitary group $\mathrm U(k)$ with highest weight $U^z_\tau-\rho$ for the diagonal torus and the positive roots $e_a-e_b$, $a<b$. Put $$c_z=\frac{v_N(z)\,v_H(z)}{\prod_{\tau\in\mathcal T}\dim\pi_{z,\tau}},\qquad K_z=\frac{1}{c_z}\,P_z^{*}P_z\ \in\ \operatorname{End}_{\mathbb C}(C_z),$$ where $P_z^{*}:H_{\rm mom}\to C_z$ is the adjoint of $P_z$. We call $K_z$ the *normalized Gram operator* of the source $z$. For an endomorphism $A$ of $C_z$, $\|A\|_{\rm HS}^2=\operatorname{tr}(A^{*}A)$ is the square of its Hilbert–Schmidt norm.

**The standing conditions.** Let $L,C',C_\ell,C_g,c_b,C_u,c_T,C_T$ be real numbers. The datum $D$ satisfies the *standing conditions of the diagonal estimate at scale $L$ with constants $(C',C_\ell,C_g,c_b,C_u,c_T,C_T)$* if the following seven conditions hold.

**(P) Origin.** The datum $D$ is assembled by the construction of the proof from base data, auxiliary data that include elements of $\mathcal O_E$ of norms $g_0$, $g_1$ and $T_z$, column data satisfying the compatibility laws of the construction, and data of its later stages. For these choices there exist, in addition, symmetric finite levels and column identifications for $D$ ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)) and a spectral realization of $D$ ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)), subject to the further compatibility conditions of the construction. Among these conditions are the finite spectral condition (condition 7 of [Conditions on linked records for the period identity](https://andrewodesky.com/rh/lean/GlobalTheory.Fam.BundlePointConditions/)), the local comparison (2) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)), and the requirement that the CM field of the spectral realization is $E$ and that its identification with $E$ is the identity map.

**(S) Scale and sizes.** There are size data $S$ for $D$, with scale parameters $x>1$ and $0<\varepsilon<1/52$ and constant $C_\Gamma(S)$, such that $$x^{\varepsilon}=L,\qquad C_\Gamma(S)\ge1,$$ and such that the pair $(D,S)$ satisfies the size conditions (S1)–(S20) of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)) with constants $(C',C_\ell,C_g,c_b,C_u,c_T,C_T)$. In particular $8\,C_\Gamma(S)\le C'$ and $C'm^5fL\le k$.

**(W) Weights and primes.** The datum $D$ satisfies conditions (N1)–(N9) and (N11)–(N13) of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)); these twelve conditions do not involve the constant $C_0$ of that page. Moreover $d_z>0$ for every source $z$.

**(R) Dimensions.** For every source $z$, $$d_z=d^*_z\,\bigl(T_z^{\,k}-1\bigr)^{f}.$$

**(C) Comparisons.** The six conditions of ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)) hold for $D$.

**(M) Mass identities.** Let $(V,h)$ be a Hermitian space over $E$ and $\Lambda\subset V$ an $\mathcal O_E$-submodule that is the $\mathcal O_E$-span of a basis of $V$ orthonormal for $h$. Write $\operatorname{mass}(\Lambda)$ for the mass of the genus of $\Lambda$, as defined in ([The record of conditions on a class of families that the final argument takes as input](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)). If $\dim_E V=k$, then for every source $z$ $$d_z=\operatorname{mass}(\Lambda)\cdot\prod_{\mathfrak p}\prod_{i=1}^{k}\bigl(N\mathfrak p^{\,i}-1\bigr)\cdot\prod_{\tau\in\mathcal T}\frac{\prod_{0\le a<b<k}\bigl(U^z_{\tau,a}-U^z_{\tau,b}\bigr)}{\prod_{i=0}^{k-1}i!}\cdot\bigl(T_z^{\,k}-1\bigr)^{f}.$$ If $\dim_E V=r$, then $$D_*=\operatorname{mass}(\Lambda)\cdot\prod_{\mathfrak p}\frac{\prod_{i=0}^{r-1}\bigl(N\mathfrak p^{\,r}-N\mathfrak p^{\,i}\bigr)}{N\mathfrak p^{\,r_S(2k+2r_S+1)+k(k-1)/2}}\cdot\prod_{\tau\in\mathcal T}d_\tau.$$ In both identities $\mathfrak p$ runs over the prime ideals of $\mathcal O_F$ that contain $g_0$ or $g_1$, and $N\mathfrak p$ is the absolute norm.

**(F) Size of the source primes.** For every source $z$, $$T_z\Bigl(\frac{2\pi}{\operatorname{rd}_E\,g_0\,g_1}\Bigr)^{2r_S}\ge1.$$
