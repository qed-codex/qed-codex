---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/StabilizerVolume/InVolumesAtOfSWS.lean",
  "declarations": [
    "PI.VolStabS.MassDataS.SWXS"
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

## Three inputs for the selected off-diagonal bound

[Definition / hypothesis THETA.D060](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)

The three statements below are hypotheses of estimates for sums of geometric terms. A datum is a choice of data satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)); its fields $F\subset E$, integers $k,m,f$, $r=k+m-1$, $r_S=m/2-1$, primes $g_0,g_1$, source words $u$ with primes $T_u$ and dimensions $d_u$, embeddings $\tau\in\mathcal T$ with positive numbers $d_\tau$, rows $U^u_\tau$ of the weight arrays, the function $\operatorname{Vand}$ and the real number $D_*$ are as in ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)).

**(1) The Siegel–Weil formula for the unitary groups of automorphic settings.** Let $D$ be a datum and $X$ an automorphic setting on $D$, in the sense of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)). The setting contains a CM extension $E'/F'$ with its conjugation, an integer $n$ and a nonsingular Hermitian matrix $J\in M_n(E')$. The statement is: for every such $D$ and $X$, assertions (a) and (b) of ([Hypothesis: the Siegel-Weil formula for unitary groups over a CM extension, for nondegenerate Fourier coefficients in the range M \> 2n](https://andrewodesky.com/rh/lean/HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent/)) hold for $F'$, $E'$, the conjugation, $M=n$ and $J$.

**(2) The local comparison for a datum.** Let $D$ be a datum. For every nonzero prime $\mathfrak p$ of $\mathcal O_F$, with residue characteristic $\ell$, the datum contains the local data of ([Moment data for the family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.Draft.SData/)): a local field $F_{\mathfrak p}$ with a continuous algebra map $\mathbb Q_\ell\to F_{\mathfrak p}$, a two-dimensional $F_{\mathfrak p}$-algebra $E_{\mathfrak p}$, maps $\iota_F:F\to F_{\mathfrak p}$ and $\iota_E:E\to E_{\mathfrak p}$, the automorphism $c_{\mathfrak p}$, the subring $O_{\mathfrak p}\subset E_{\mathfrak p}$ of elements integral over the valuation ring of $F_{\mathfrak p}$, and the additive character $\psi_{\mathfrak p}$. The *standard local data* at $\mathfrak p$ are the completion $F^c_{\mathfrak p}$ of $F$ at $\mathfrak p$ and $E^c_{\mathfrak p}=F^c_{\mathfrak p}\otimes_FE$, with the maps, topology, involution, integral subring and standard character described in the last part of Hypothesis (measures) of ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)).

The *local comparison holds for $D$* if for every $\mathfrak p$ there are ring isomorphisms $$e_F:F_{\mathfrak p}\xrightarrow{\ \sim\ }F^c_{\mathfrak p},\qquad e_E:E_{\mathfrak p}\xrightarrow{\ \sim\ }E^c_{\mathfrak p}$$ with the following properties.

- $e_F$ and $e_F^{-1}$ are continuous; $e_F\circ\iota_F$ is the inclusion of $F$ in $F^c_{\mathfrak p}$; $e_F$ commutes with the maps from $\mathbb Q_\ell$; and for all $x,y\in F_{\mathfrak p}$, $|x|\le|y|$ in $F_{\mathfrak p}$ if and only if $|e_F(x)|\le|e_F(y)|$ in $F^c_{\mathfrak p}$.
- $e_E$ and $e_E^{-1}$ are continuous; $e_E(a\cdot1)=e_F(a)\cdot1$ for $a\in F_{\mathfrak p}$; $e_E\circ\iota_E$ is the map $x\mapsto1\otimes x$ of $E$ into $E^c_{\mathfrak p}$; $e_E$ commutes with the two involutions; $y\in O_{\mathfrak p}$ if and only if $e_E(y)$ lies in the integral subring of $E^c_{\mathfrak p}$; and $\psi_{\mathfrak p}(y)$ is the value of the standard character at $e_E(y)$, for every $y\in E_{\mathfrak p}$.

**(3) The lattice mass identities.** Let $(V,h)$ be a Hermitian space over $E$: a vector space over $E$ with a form $h$ that is conjugate-linear in the first variable, linear in the second, and satisfies $h(y,x)=\overline{h(x,y)}$. A lattice $L\subset V$ *has an orthonormal basis of size $N$* if $L=\bigoplus_{i<N}\mathcal O_Ee_i$ for a basis $e_0,\dots,e_{N-1}$ of $V$ with $h(e_i,e_j)=\delta_{ij}$. Write $\operatorname{mass}(L)$ for the mass of the genus of $L$: the sum of $1/|\operatorname{Aut}(M)|$ over a set of representatives $M$ of the isometry classes of lattices in the genus of $L$, where the genus consists of the lattices $M\subset V$ such that for every maximal ideal $\mathfrak q$ of $\mathcal O_E$ some isometry of $V$ carries the localisation of $L$ at $\mathfrak q$ to that of $M$, and $\operatorname{Aut}(M)$ is the group of isometries of $V$ preserving $M$.

Let $\mathfrak p$ range over the primes of $\mathcal O_F$ that divide $g_0g_1$, write $\mathrm N\mathfrak p$ for the absolute norm, and put $$G_D=\prod_{\mathfrak p\mid g_0g_1}\ \prod_{i=1}^{k}\bigl(\mathrm N\mathfrak p^{\,i}-1\bigr),\qquad I_D=\prod_{\mathfrak p\mid g_0g_1}\frac{|\mathrm{GL}_r(\mathbb F_{\mathrm N\mathfrak p})|}{\mathrm N\mathfrak p^{\,r_S(2k+2r_S+1)}\ \mathrm N\mathfrak p^{\,k(k-1)/2}} .$$ The *lattice mass identities hold for a datum $D$* if for every Hermitian space $(V,h)$ over $E$ and every lattice $L\subset V$:

- if $L$ has an orthonormal basis of size $k$, then for every source word $u$ $$d_u=\operatorname{mass}(L)\cdot G_D\cdot\prod_{\tau\in\mathcal T}\frac{\operatorname{Vand}(U^u_\tau)}{\prod_{i=0}^{k-1}i!}\cdot\bigl(T_u^{\,k}-1\bigr)^{f};$$
- if $L$ has an orthonormal basis of size $r$, then $$D_*=\operatorname{mass}(L)\cdot I_D\cdot\prod_{\tau\in\mathcal T}d_\tau .$$

Let $\mathcal C$ be a class of families and $C_0$ a real number. The *lattice mass identities hold along $\mathcal C$ with constant $C_0$* if the following is true for all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal C$, in the sense of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)): there is $x_0$ such that for every real $x\ge x_0$ and every $i\in I_x$ at which the family standing conditions with constant $C_0$ of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)) hold, the lattice mass identities hold for $D(x,i)$.
