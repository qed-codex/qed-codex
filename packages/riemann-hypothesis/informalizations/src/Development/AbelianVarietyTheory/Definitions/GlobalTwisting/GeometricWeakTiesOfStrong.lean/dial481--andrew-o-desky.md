---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/GeometricWeakTiesOfStrong.lean",
  "declarations": [
    "GlobalTheory.Fc.S0.NL"
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

## The record of conditions on a class of families that the final argument takes as input

[Definition / hypothesis ANT.D031](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.HypsAlt/)

This entry describes the record whose existence is the conclusion of the theorem ([A class of families satisfying the input conditions of the final argument exists, given hypothesis list A, the rationality test, the norm bound at 2 and 3, a maximal slope bound and a covolume bound](https://andrewodesky.com/rh/lean/GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt/)). It uses the vocabulary of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)): datum, size data, family with parameter $\varepsilon$, member $(x,i)$, class of families, its refinements $\mathcal{C}'$ and $\mathcal{C}''$, the standard conditions (N1) to (N4) and (a) to (j), and "holds for all sufficiently constrained families of a class".

The record consists of six pieces of data and forty conditions. Conditions (3), (16), (25), (33), (35) and (37) are stated in part or wholly by their logical form: each contains terms, marked "(not expanded)", that have no definition on this page or on a page it cites. Every other condition is stated in full, in standard terms or in the terms of the entries it cites.

**Tuples.** A datum contains a set whose elements we call *tuples*, with a base tuple $\mu_0$, and assigns a tuple $\mu_w$ to every finite place $w$ of $\Lambda$.

**Attached records and selections.** An *object* over a datum $D$ consists of size data $L$ for $D$ and seven further records; a member $(x,i)$ of a family with $x>x_1$ gives a datum $D(x,i)$ and an object $O(x,i)$ over it. For a datum $D$, an object $O$ and a real number $c$, an *attached record over $(D,O,c)$* has the following seven components.

- A *realisation*: data of ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)) for $D$ and $O$, with four further conditions (not expanded).
- *Spectral data*: a spectral realization of $D$, in the sense of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)), with nine further items that tie it to the realisation; one of them is the local comparison of item (2) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)), and the other eight were not expanded.
- A *row-side family*: data of ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)) for $D$ and $O$. It contains a rational family in the sense of ([Class sums and finite Hecke families](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.CSD/)) and, at the base level, a finite set $\mathrm{Tw}_0$ of primes of $\Lambda$.
- A condition relating the realisation to the row-side family (not expanded).
- A pair of natural numbers $(p_1,p_2)$ such that $p_1$ equals a rational component of $D$ and $m\,p_2$ equals a real component of $L$.
- A record of column data for the realisation and the row-side family (not expanded).
- An *analytic part*, which depends on all the preceding components and on $c$. It contains analytic and rational realization data for the rational family, in the sense of ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)), and a face, in the sense of ([Rational families of forms, their realisations by theta maps, and the rationality test](https://andrewodesky.com/rh/lean/Formalism.IndefR.Rat.RowTest/)); its other components were not expanded.

A *selection* on a class $\mathcal{A}$ assigns to every family $\mathrm{Fm}$ in $\mathcal{A}$ and every member $(x,i)$ with $x>x_1$ an attached record over $(D(x,i),O(x,i),C_{sz})$, called the *selected record* at the member. The spectral realizations contained in the selected records form a selection of spectral realizations on $\mathcal A$, with thresholds $x_\sigma(\mathrm{Fm})=x_1$, in the sense of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)); we call it the *spectral selection of $\sigma$*.

**Data.**

- a class of families $\mathcal{A}$;
- a selection $\sigma$ on $\mathcal{A}$;
- a function $c_T\colon\mathbb{R}\times\mathbb{R}\to\mathbb{R}$;
- a function $c_{30}$ that assigns to every finite list of real numbers seven constants, of which five are used below: $n_0\in\mathbb{N}$ and $A_0,C_0,c_0,c_b\in\mathbb{R}$;
- for every family in $\mathcal{A}$ and every member with $x>x_1$, a record with 10 components that relates components of the selected record to components of the datum (not expanded; no condition below refers to it);
- a real number $c_I$.

**Conditions.** The conditions are numbered 1 to 40 in the order of the record and are grouped here by the families they concern. "Eventually at the members" means: there is $x_0$ such that the statement holds at every member $(x,i)$ with $x\ge x_0$ and $x>x_1$.

*Existence of families.*

**(1)** Suppose that for every $j$ the order of every finite subgroup of $\mathrm{GL}_j(\mathbb{Q})$ divides Minkowski's number $M(j)$. Let $\lambda>1$ and let $G$ be a property of field data for which the supply condition with exponent $\lambda$ holds, in the sense of ([Properties of field data, their supply condition and their classes of families](https://andrewodesky.com/rh/lean/UpperTheory.Top.FReq/)); let $\mathcal E(G,\lambda)$ be the class of families defined there. Then there is $\varepsilon_0>0$ such that for every $0<\varepsilon\le\varepsilon_0$ and every threshold $K$ there are a family $\mathrm{Fm}$ with parameter $\varepsilon$ and real numbers $C_H\ge 0$, $C_5>0$, $C_b>0$ with the following properties.

- $\mathrm{Fm}$ belongs to $\mathcal A$ and to $\mathcal E(G,\lambda)$ and satisfies (g).
- $\mathrm{Fm}$ is large for $K$ with $C_H$, its constant $C_F$ equals $C_H$, and $c_T(\varepsilon,C_{YL})\le C_{Tu}$.
- $\mathrm{Fm}$ satisfies (a), (b), (c), (d) and (e).
- There is $x_0$ such that the five statements (1a) to (1e) hold at every member $(x,i)$ with $x\ge x_0$.

In (1a) to (1e) the sets $TT$ and $T_2$, the integers $n_0$ and $L_w$ and the real constant $C_2$ are those of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), $W$ is the set of words, and $C_\Gamma$ is the positive real constant of ([Shared data in an arithmetic family](https://andrewodesky.com/rh/s/family-shared-data.html)).

(1a) $\displaystyle\frac{n_0\exp\bigl(-C_2\sqrt{\log n_0\,\log L_w}\bigr)}{L_w}\le|T_2|$.

(1b) $\tfrac12\delta_1n\le|TT|\le2\delta_1n$.

(1c) Let $\mathcal P_x$ be the set of primes $p<X'$ of the inert class of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)) with $\nu_p\ge x^{\varepsilon/4}$. For $p\in\mathcal P_x$ call $t\in TT$ *bad at $p$* when the representative $z=s(h_p,t)$ of the coset $t+\langle h_p\rangle$ fails one of the conditions 1 to 3 on a representative in the paragraph "The weighted prime sum in (N4)" of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)), formed with $\nu=\nu_p$ and $T_z=\{0\le i<\nu_p:z+ih_p\in TT\}$; here $s$ is the map that the family supplies at the member. Then $$\sum_{p\in\mathcal P_x}\frac{\log p}{p}\,\bigl|\{t\in TT:t\text{ is bad at }p\}\bigr|\ \le\ 4C_b\,x^{-2}\,\delta_1n\sum_{p\in\mathcal P_x}\frac{\log p}{p}.$$

(1d) Every primitive Dirichlet character $\chi$ that agrees on the integers coprime to $8qd$ with $a\mapsto\left(\frac{-q}{a}\right)$, with $a\mapsto\left(\frac{-d}{a}\right)$ or with their product satisfies $$|g_\chi(x)|\le x^{1/2+\varepsilon},\qquad|\kappa_\chi|\le C_5\log x,$$ where $\kappa_\chi=L'(1,\chi)/L(1,\chi)$ and $g_\chi$ is the function of ([Compatible arithmetic data on intervals](https://andrewodesky.com/rh/lean/UpperTheory.Top.topDesWin/)).

(1e) With $\Gamma=\exp\bigl(C_\Gamma\,m^5f\,\mathcal L\bigr)$, $$3\,\Gamma^2x^{C_H}\ \le\ |W|\ \le\ 3\,\Gamma^2x^{C_H}+1.$$

*Conditions on every family in $\mathcal{A}$.*

**(2)** The family satisfies (N1), (N2), (N3), (N4) and (b), and the following two statements hold eventually at the members.

(2a) Every tuple is one of $\mu_0$, $\mu_*$, $\mu_*'$ or $\mu_w$ for a place $w$ of $\Lambda$, where $\mu_*$ and $\mu_*'$ are the two further distinguished tuples of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)).

(2b) There are natural numbers $N_0(i)$ and finite sets $S_{i,j,b}$ as in Hypothesis (integral twisting) of ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)) for which all requirements of that hypothesis at a member hold, and continue to hold, with the same $N_0(i)$ and $S_{i,j,b}$, when at each place $w$ with $\mu_w\ne\mu_0$ the character $\psi'_w$ is replaced by $(\psi'_w)^a$, for every integer $a$ prime to the prime $\ell_{i_w}$ of the twist index $i_w$.

**(3)** At every member with $x>x_1$, the analytic part of the selected record satisfies two conditions (not expanded): for every stage there is a vector of an archimedean model that is extremal and is paired to a prescribed vector; and for every stage a condition of the kind of Hypothesis (one-map rows) of ([Geometric theta class evaluations](https://andrewodesky.com/rh/lean/Formalism.IndefR.FWT.OMPins/)) holds for the realization data of the analytic part.

**(4)** At every member with $x>x_1$, every prime $y$ of $\Lambda$ in the set $\mathrm{Tw}_0$ of the row-side family of the selected record lies in the finite set $\mathcal S$ of places of ([Local size and support data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.SizeData%E2%82%82/)) and has $\mu_y\ne\mu_0$.

**(5)** At every member with $x>x_1$: the primitive row comparisons of ([Analytic theta maps and primitive row comparisons](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)) hold for the realization data and the face in the analytic part of the selected record; and the rational family of its row-side family satisfies the separation of types stated as conclusion (B) of ([Properties of the theta maps of a realised rational family: Hecke equivariance, inner product identities, rationality, and separation of Hecke types](https://andrewodesky.com/rh/lean/GlobalTheory.Closing3.primRows3_typesSep3_alt/)).

**(6)** At every member with $x>x_1$ the following holds for the row-side family of the selected record. Its base level $b=0$, its set $\Pi$ of full labels, its distinguished infinite place $v_0$, the subspaces $W_{0,i,\pi}$ and $E_{0,\pi}$ and the real scalars $\lambda_{0,i,t,\pi,v}$ are those of ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)); the map $\tau$ from the twists of the row-side family to the tuples of the datum and the semilinear maps $J_i\colon\Lambda^{d_{W,i}}\to M_{i+1}$, for $0\le i<m$, are those of ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)); the set $\mathcal F$ of type labels, the subspaces $M_{j,\sigma}\subseteq M_j$, the real numbers $\lambda_{\mu,j,\sigma}$ and the labels $\pi^0_a\in\mathcal F$ of the basis $(h^0_a)_{0\le a<D_0}$ of $H_0$ are those of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). A tuple is *used* if it is $\mu_0$ or equals $\mu_w$ for some finite place $w$ of $\Lambda$. There is a map $c\colon\mathcal F\to\Pi$ such that:

(6a) for $1\le j\le m$ and every $\pi\in\Pi$, the subspaces $M_{j,\sigma}$ with $c(\sigma)=\pi$ are linearly independent and their sum is the complex span of $J_{j-1}(W_{0,j-1,\pi})$;

(6b) for $1\le j\le m$, every twist $t$ such that $\tau(t)$ is used, and every $\sigma\in\mathcal F$ with $M_{j,\sigma}\ne0$: $\lambda_{\tau(t),j,\sigma}=\lambda_{0,j-1,t,c(\sigma),v_0}$;

(6c) for every $\pi\in\Pi$, the number of indices $a<D_0$ with $c(\pi^0_a)=\pi$ equals $\dim_\Lambda E_{0,\pi}$.

**(7)** At every member with $x>x_1$, the row-side family of the selected record satisfies the following parts of Hypothesis (divisor row comparisons) of ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)), in the notation of that entry.

(7a) At the sharp level and at the base level, the isomorphisms $e_R$ and $e_R^0$ identify the integral row lattices and every archimedean Hermitian form: $e_R(R_1)=R$, $e_R^0(R_0)=R^0$, and the two displayed identities for $Q_v$ and $Q_v^0$ hold at every infinite place $v$.

(7b) For every stage $0\le i<m$ and every twist $t$ such that $\tau(t)$ is used, the selected complex input space $Z_{\tau(t),i+1}$ is the complex span displayed there.

(7c) For every stage $0\le i<m$, every twist $t$ such that $\tau(t)$ is used and every $x$: $\theta^P_{\tau(t),i+1}\bigl(J^{\rm in}_{\tau(t),i+1}(e_{i,t}x)\bigr)=J_i(\theta_{i,t}\pi_{i,t}x)$.

(7d) For every stage $0\le i<m$, every finite place $w$ and every twist $t$ such that $\tau(t)$ is used: $I_{\tau(t),i+1,w}=[M_i:\theta_{i,t}(T_{i,t})]_w$ and $J_{\tau(t),i+1,w}=[T_{i,t}:T_{i,t}^{\#}]_w$. For every stage $0\le i<m$ and every finite place $w$, the number $\eta_{i+1,w}$ is zero off the twisted set of the base level and is given there by the displayed length.

(7e) For every word $u$: $B_u(e_{N,u}x,e_Ry)=B^{\rm col}_{w(u)}(x,y)$ for all $x,y$.

**(8)** At every member with $x>x_1$: for every word $u$, every twist $t$ of the row-side family of the selected record such that $\tau(t)$ is used, every $x\in\Lambda^{a_{w(u)}}$ and every $F\in\Lambda^{n_{1,t}}$, $$\jmath\bigl(p_{w(u),t}(x,F)\bigr)=P_{u,\tau(t)}\bigl(j^N_u(e_{N,u}x),\ j^A_t(r_tF)\bigr).$$ Here $p_{u',t}\colon\Lambda^{a_{u'}}\times\Lambda^{n_{1,t}}\to\Lambda$ are the pairings of ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)); $u\mapsto w(u)$, the isomorphisms $e_{N,u}$ onto the $\Lambda$-space of the source lattice of $u$, and the semilinear map $j^A_t$ from the sharp row coordinates at $t$ to $A_{\tau(t)}$ are those of ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)); $P_{u,\mu}$ is the pairing of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)) and $j^N_u$ the semilinear map from the $\Lambda$-space of the source lattice to $U_u$ of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)); and $r_t$ is the matrix that expresses the chosen basis of the right coordinates $\Lambda^{n_{1,t}}$ of the sharp level in the coordinates of the image of the idempotent $e_{P_1,\psi_1}$.

**(22)** At every member with $x>x_1$ the following four statements hold. They use the notions of ([Normalised Haar measures on the adelic unitary groups of Hermitian spaces over the CM field, and the volume function of a datum](https://andrewodesky.com/rh/lean/Formalism.MainNotions.StandardLattice.IsVolMeas/)).

(22a) Let $W$ and $W_0$ be Hermitian spaces with recorded lattice data over $E$ of the same rank, of signatures $(P,Q)$ and $(P_0,Q_0)$. Let $\mu$ and $\mu_0$ be measures on $H_W(\mathbb A_F)$ and $H_{W_0}(\mathbb A_F)$ normalised for $(P,Q)$ and $(P_0,Q_0)$, and let $\mathcal F$ and $\mathcal F_0$ be fundamental domains for the actions of $H_W(F)$ and $H_{W_0}(F)$ with respect to them. Then $\mu(\mathcal F)=\mu_0(\mathcal F_0)$.

In (22b) to (22d), $n_Y$ is the rank of the space $Y_0$ of ([Hermitian spaces in the theta constructions](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.CMData/)), and $W$ is any Hermitian space with recorded lattice data over $E$ of rank $n_Y$ and signature $(n_Y,0)$, with recorded lattice $L_0$.

(22b) The genus of $L_0$ has the same mass as the genus of $\mathcal{O}_E^{\,n_Y}$ for the form $\sum_i\bar x_iy_i$.

(22c) There are finitely many elements $g_1,\dots,g_c$ of $H_W(\mathbb A_F)$ such that $H_W(\mathbb A_F)$ is the disjoint union of the double cosets $H_W(F)\,g_i\,K_W$.

(22d) For every finite list $g_1,\dots,g_c$ as in (22c), $$\sum_{i=1}^{c}\frac1{\bigl|\{\gamma\in H_W(F):g_i^{-1}\gamma g_i\in K_W\}\bigr|}$$ is the mass of the genus of $L_0$.

**(24)** There is $x_0$ such that at every member with $x\ge x_0$ and for every tuple $\mu$, the integral span $\widetilde M_\mu\subseteq A_\mu$ of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)) is stable under multiplication by $\jmath(a)$ for every $a$ in the ring of integers of $\Lambda$, where $\jmath\colon\Lambda\to\mathbb C$ is the embedding of the datum.

*Conditions on the first refinement.* Each of the next two holds for all sufficiently constrained families of $\mathcal{A}'$.

**(9)** If $c_T(\varepsilon,C_{YL})\le C_{Tu}$ then (i) holds.

**(10)** At every member with $x>x_1$: suppose that $2fk<g_i-1$ for some $i\in\{0,1\}$ and that each of $g_0$, $g_1$ splits completely in $F$. Then for every word $u$ whose prime $T_u$ splits completely in $F$, the first class set $C_0(u)$ of the column chain of $u$, in the notation of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), satisfies $$|C_0(u)|=\operatorname{mass}(\mathcal{O}_E^{\,k})\cdot\bigl[\mathrm{GL}_k(\mathbb F_{g_0}):N_k(\mathbb F_{g_0})\bigr]^{f}\bigl[\mathrm{GL}_k(\mathbb F_{g_1}):N_k(\mathbb F_{g_1})\bigr]^{f}\cdot\bigl(T_u^{\,k}-1\bigr)^{f}.$$ Here $F$ is the maximal real subfield of $E$, of degree $f$ over $\mathbb Q$; a prime $p$ splits completely in $F$ when exactly $f$ prime ideals of $\mathcal O_F$ lie above $p$, each with residue field of $p$ elements; $N_k$ is the group of upper triangular matrices with diagonal entries $1$; and $\operatorname{mass}(\mathcal{O}_E^{\,k})$ is the mass of the genus of the lattice $\mathcal{O}_E^{\,k}$ for the Hermitian form $\sum_i\bar x_iy_i$ on $E^k$.

*Conditions on the second refinement.* Each of the following, except (19), holds for all sufficiently constrained families of $\mathcal{A}''$; the hypothesis cited in (19) has this form itself, with one function fixed first.

**(14)** There is $x_0$ such that at every member $(x,i)$ with $x\ge x_0$ at which the family standing conditions with constant $3$ hold, in the sense of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)), every word $w$ satisfies $$1\le T_w\Bigl(\frac{2\pi}{\operatorname{rd}_E\,g_0g_1}\Bigr)^{m-2},$$ where $\operatorname{rd}_E=|\operatorname{disc}E|^{1/[E:\mathbb Q]}$.

**(19)** Hypothesis (row bounds for pairs of terms along a selection) of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)) holds with constant $3$ for the class $\mathcal A''$ and the spectral selection of $\sigma$.

**(20)** There is $x_0$ such that at every member $(x,i)$ with $x\ge x_0$ and $x>x_1$ at which the family standing conditions with constant $3$ hold, every two distinct words $u\ne u'$ satisfy $$\bigl\|K^0_{u,u'}\bigr\|_{\rm HS}^{2}\ \le\ \bigl(1+b^{-6}\bigr)\,\frac{d_u\,d_{u'}}{D_*}.$$ Here $K^0_{u,u'}$ is the sum of term operators of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)), formed with the automorphic setting and the completion of the spectral realization in the selected record, and $d_u$, $D_*$ are the numbers of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)).

**(21)** With $(n_0,A_0,C_0,c_0,c_b)$ taken from $c_{30}(c_{\mathrm{out}})$, the restricted counting condition of ([Multiplicity estimate at the selected character level](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.CountE.CountAllPointsClass/)) holds for the family and the constants $n_0$, $A_0$, $C_0$, $c_0$, $c_b$. In particular $c_0>0$ and $c_b>0$.

**(23)** There is $x_0$ such that at every member with $x\ge x_0$ the following holds. In the notation of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), let $\iota_{\mu_0}\colon A_{\mu_0}\to H$ be the composite of the inverse of the isometry $V_{\mu_0,m}\simeq A_{\mu_0}$, the maps $i_{\mu_0,m-1},\dots,i_{\mu_0,0}$ from $V_{\mu_0,m}$ down to $V_{\mu_0,0}$, and the isometry $V_{\mu_0,0}\simeq H$. Then $\iota_{\mu_0}$ maps the image of the idempotent $e_{\mu_0}$ onto $H$.

**(25)** With the real number $C_H$ of the definition of "sufficiently constrained": there is $C\ge 0$ such that eventually at the members the selected record satisfies nine conditions with the constants $(C,C_H)$ and the definite-side condition with $(C,C_H)$. The nine conditions concern two coordinate data that the analytic part of the selected record determines, and numerical data $F_0$, $J_0$, $E_1$, $l_3$, $l_6$, $h$ formed from the analytic part with $C$ and $C_H$; the coordinate data and the numerical data are of the kind chosen for a level in ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)), whose notation is used here with the index of the level omitted (their construction from the analytic part was not expanded). Five of the nine conditions read as follows.

(25a) *Covolume.* For the first coordinate datum and every stage $i$: $\operatorname{lcv}(M_{W,i})/d\le l_3(i)$, where $d$ is the common dimension and $\operatorname{lcv}$ the normalised logarithmic covolume of ([Base target slope from determinant and local index bounds](https://andrewodesky.com/rh/lean/Formalism.L2.Indef.IndefSide.boundsMu/)). This has the form of the inequality of ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)).

(25b) *Local indices.* Suppose that the defect condition of ([Integral maps with height and target bounds](https://andrewodesky.com/rh/lean/Formalism.MainNotions.LinkDIV_at/)) holds for the family. Then, for the first coordinate datum, with $I_{i,w}=[M_{W,i}:\Theta_{i,\mu(w)}(T_{i,\mu(w)})]_w$ the relative local index at $w$ of $M_{W,i}$ and of the image of the module $T_{i,\mu(w)}$: at every place $w$ of the twisted set $\mathrm{Tw}$, $$\sum_i\bigl(I_{i,w}+I_{i,\bar w}\bigr)\le d\Bigl(\sum_i\bigl(2e_wF_0(w,i)+e_w\operatorname{err}_{w,i}\bigr)+\frac{2e_w}{p_w^2}\Bigr),\qquad\operatorname{err}_{w,i}\ge0,$$ and for every stage $i$, $\sum_{w\in\mathrm{Tw}}\ell_we_w\bigl(\operatorname{err}_{w,i}+J_0(\mu(w),w,i)\bigr)\le E_1(i)$, with $\ell_w=\log\mathrm N\mathfrak p_w/[\Lambda:\mathbb Q]$.

(25c) *Slope.* Under the same supposition, for the first coordinate datum, $\mu_{\max}(R)\le h-\overline{\log\kappa}$, where $R$ is its row lattice, $\mu_{\max}$ the maximal slope and $\overline{\log\kappa}$ the mean of $\log\kappa_v$ over the infinite places $v$ of $\Lambda$.

(25d) *Scalars.* Suppose that the second condition of (3) holds at the member. Then, for the second coordinate datum, $l_6(i)\le\log\lambda_{i,t_0,\pi,v}$ for every stage $i$, every full label $\pi$ and every infinite place $v$, where $t_0$ is the distinguished twist.

(25e) For every embedding $\sigma\colon\Lambda\to\mathbb C$, the coefficient $\kappa_R(\sigma)$ of ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)) equals the scalar $\kappa_{1,v}$ of the sharp level of the row-side family of the selected record at the place $v$ of $\sigma$.

The other four of the nine (a containment of a set of places in the twisted places, two conditions on a conjugate-linear map into a Hilbert space, and a condition on the passage between two levels) were not expanded. The definite-side condition says: under four conditions on the selected record that involve $C$ and $C_H$, for all real numbers $\lambda_0,C_0',c_e,S_w,C_1$ satisfying a numerical condition for each word, and all families of $\mathcal{O}_\Lambda$-modules and compatibility data that match those of the selected record, for every word there are a record of a kind not expanded and invertible matrices at the infinite places of $\Lambda$ satisfying an operator-norm bound, further bounds and non-degeneracy conditions (the statement was read; its terms were not expanded).

*Conditions on the second refinement, continued: the terminal map and the period pairing along the chains of the words.* Conditions (26) to (31) use the notation of ([Rational forms along the column chain of a word: lattices, twisted chains, the terminal map and valuations at a place](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms.PRat/)): for a word $u$, the lattices $\mathcal L_i$ and $\mathcal L_P$ with their maps $j_i$, $j_P$, the terminal map $\operatorname{pt}_u$, the twisted chain and twisted forms of $(u,\mu)$, the local lattice $N^T_{u,w}$, and the two notions of valuation at a place. The twisted forms, the finite sets of primes $Q_\mu$ of ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)) and the elements $\pi_0,\pi_1$ of ([Local error functions and weight normalizations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ErrC/)) are those that the family supplies at the member. Each of (26) to (30) says: there is $x_0$ such that the statement holds at every member $(x,i)$ with $x\ge x_0$ and $x>x_1$.

**(26)** For every word $u$:

(26a) the map $\tau_P\colon C_P\to C_m$ is injective, and for every $c\in C_P$ the homomorphism $G^P_c\to G_{m,\tau_P(c)}$ is bijective;

(26b) $\operatorname{pt}_u(F_m)\subseteq F_P$;

(26c) the terminal map of $u$ is integral;

(26d) for every infinite place $v$ of $\Lambda$ and every $x\in(\mathcal L_m)_\Lambda$, $$\bigl\|\operatorname{pt}_u^\Lambda(x)\bigr\|_{\mathcal L_P,v}^2\le B_u\,\|x\|_{\mathcal L_m,v}^2,\qquad B_u=\prod_{\tau\in\mathcal T}T_u^{-\deg_\tau}\,b_\tau^{2},\qquad\deg_\tau=\sum_{i}\lambda_{m,\tau,i}-\sum_i\sigma_{\tau,i}-\Bigl⌊\frac{m(t+1)}2\Bigr⌋;$$

(26e) for every $\phi\in F_m$, $\operatorname{Re}q_P(\operatorname{pt}_u\phi,\operatorname{pt}_u\phi)\le B_u\operatorname{Re}q_m(\phi,\phi)$.

**(27)** For every word $u$ and every used tuple $\mu\ne\mu_0$, the terminal map of the twisted forms of $(u,\mu)$ is integral.

**(28)** Suppose that the stabiliser condition holds for the datum. Then for every word $u$, every $x\in\mathcal L_P^{\rm int}$ and every $F\in\widetilde M_{\mu_0}$ in the image of $e_{\mu_0}$ there is $y\in\Lambda$ with $$\jmath(y)=q\bigl(j_P(x),\varepsilon_u^{-1}F\bigr)$$ such that at every finite place $w$ of $\Lambda$ either $y=0$ or $v_w(y)\ge-e_w\,v_{p_w}\bigl(D_\Gamma(u)\bigr)$.

**(29)** Suppose that the stabiliser condition holds for the datum. Then for every word $u$, every used tuple $\mu\ne\mu_0$, every $x\in(\mathcal L_P^{\mu})^{\rm int}$ and every $F\in\widetilde M_{\mu}$ in the image of $e_{\mu}$ there is $y\in\Lambda$ with $$\jmath(y)=q^{\mu}\bigl(j^{\mu}_P(x),\varepsilon_{u,\mu}^{-1}F\bigr)$$ such that at every finite place $w$ of $\Lambda$ with $p_w\notin Q_\mu$ either $y=0$ or $v_w(y)\ge-e_w\,v_{p_w}\bigl(D_\Gamma(u)\bigr)$.

**(30)** For every word $u$ and every finite place $w$ of $\Lambda$ with $p_w=T_u$:

(30a) for every $c\in\Lambda^\times$ with $v_w(c)\ge e_w\,m\,E_T(u,w)$ and every $x\in N^T_{u,w}$ there is $y\in(\mathcal L_m^{\rm int})_{(w)}$ with $j_m(y)=\jmath(c)\,K^{(m)}(j_0(x))$;

(30b) for every used tuple $\mu\ne\mu_0$ with $T_u\notin Q_\mu$ and every $x\in N^T_{u,w}$ there is $y\in(\mathcal L^{\mu}_m)_\Lambda$ with $j^{\mu}_m(y)=K^{(m),\mu}\bigl(\epsilon_{u,\mu}(j_0(x))\bigr)$ that has valuation at least $-m\,E_T(u,w)$ at $w$ relative to $\mathcal L^{\mu}_m$.

**(31)** There is a real number $C_1$ for which (31a) and (31b) each hold eventually at the members. Here $a\in\{0,1\}$, $w$ is a finite place of $\Lambda$ with $p_w=g_a$, $u$ is a word with $T_u\ne g_a$, the numbers $V_{a,u,j,w}$ are those of ([Local error functions and weight normalizations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ErrC/)), $\eta$ is the weight-width parameter used there, and $$\Delta_{a,u,w}=\sum_{j=1}^{m}V_{a,u,j,w}+C_1\,f\bigl(m\,N_m(N_m+t)+m^3\eta\bigr).$$

(31a) For all such $a,w,u$, every used tuple $\mu$, every $\varphi\in M_u$ and every $F\in\widetilde M_\mu$ there is $y\in\Lambda$ with $\jmath(y)=P_{u,\mu}\bigl(j^N_u(\varphi),F\bigr)$ and either $y=0$ or $v_w(y)\ge-e_w\,\Delta_{a,u,w}$.

(31b) For all such $a,w,u$, $$\sum_{j=1}^{m}\bigl(F_{j,w}-E_{u,j,w}\bigr)\le-\Delta_{a,u,w}.$$

**(32)** There are real numbers $C_{\deg},C_g,C_T,C_G,C_d,C_I$ and $x_0$ with $C_g\ge0$ such that the following eight statements hold at every member with $x\ge x_0$ and $x>x_1$. They use the quantities $u^u_{j,\tau}$, $V_{a,u,j,w}$, $d_{\rm Fock}(j)$, $E_T(u,w)$, $W^u_\tau$, $E_d(j)$, $E_C(j,p)$, $E_I(j,p)$, the Hermitian weights $w_j(\tau)$, the weight-width parameters $S$, $\eta$ and the constant $g_{\rm err}$ of ([Local error functions and weight normalizations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ErrC/)), for a word $u$ in the place of the source $z$; the integer weights $a_t$ ($t\in TT$; the set $TT$ is the set $T$ of those entries), the numbers $b'$, $X''$ and the prime classes $\mathcal I$, $\mathcal S$ of ([Local size and support data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.SizeData%E2%82%82/)); the integer $D_\Gamma(u)$ of the column chain of $u$; and $B_0=f\,m\,b\,x^{\varepsilon}$. For a finite place $w$ and a real $y$ put $[y]_w=2\ell_we_wy$ with $\ell_w=\log\mathrm N\mathfrak p_w/[\Lambda:\mathbb Q]$, and for $1\le j\le m$ put $$G_j=2\sum_{\tau\in\mathcal T}w_j(\tau)+C_{\deg}\Bigl(f\bigl(kS+m\,t\,\eta+kN_m\bigr)+\frac{|T|\,b'}{x}\Bigr).$$

(32a) $g_0\ne T_u$ and $g_1\ne T_u$ for every word $u$.

(32b) For $a\in\{0,1\}$, every word $u$ and $1\le j\le m$: $\displaystyle\sum_{w:\,p_w=g_a}[V_{a,u,j,w}]_w=\Bigl(\sum_{\tau\in\mathcal T}u^u_{j,\tau}\Bigr)\log g_a$.

(32c) For every word $u$ and $1\le j\le m$: $\displaystyle\Bigl|\sum_{\tau\in\mathcal T}u^u_{j,\tau}-d_{\rm Fock}(j)-\sum_{t\in TT}a_t\Bigr|\le G_j$.

(32d) For $a\in\{0,1\}$, every word $u$ and $1\le j\le m$: $\displaystyle\Bigl(G_j+2\,v_{g_a}\bigl(D_\Gamma(u)\bigr)+2\,g_{\rm err}\,f\,(N_m^2+m^2\eta)\Bigr)\log g_a\le C_g\,B_0$.

(32e) For every word $u$, with $E^{*}_T(u)=2\sum_{\tau}W^u_\tau+fN_m+|TT|(t+1)(m+1)/4$: every finite set $S$ of places of $\Lambda$ above $T_u$ satisfies $0\le\sum_{w\in S}[E_T(u,w)]_w\le E^{*}_T(u)\log T_u$, and $E^{*}_T(u)\log T_u\le C_T\,B_0$.

(32f) $2\log D_\Gamma(u)\le C_G\,B_0$ for every word $u$.

(32g) $2\log d\cdot|E_d(j)|\le C_d\,B_0$ for $1\le j\le m$.

(32h) For $1\le j\le m$ and every finite set $P$ of primes $p\le X''$ in $\mathcal I\cup\mathcal S$, $$\sum_{p\in P}2\log p\cdot\bigl|E_{CI}(j,p)\bigr|\le C_I\,B_0,$$ where $E_{CI}(j,p)=E_C(j,p)$ if $p\in\mathcal I$ and the Frobenius step $h_p$ is $0$, and $E_{CI}(j,p)=E_I(j,p)$ otherwise.

**(33)** Two statements about the kernels of the stages; apart from (ii) and (iii) below they are stated by their form only.

(33a) Eventually at the members there is a choice of local chains for which the integral comparisons of the member are compatible with its twisted forms and a condition on the size data, the orbit data, the divisor data, the levels and the elements $\pi_0,\pi_1,\pi_u$ of the member holds with constant $1$ (two conditions, not expanded).

(33b) At every member with $x>x_1$, the kernel record contained in the realisation of the selected record satisfies ten conditions. It supplies, for every word $u$, tuple $\mu$, finite place $w$ of $\Lambda$, stage $0\le i<m$ and classes $c$, $c'$ of the twisted chain of $(u,\mu)$ at the stages $i$ and $i+1$, a power series over $\mathbb C_{p_w}$ in variables indexed by $(\{0,1\}\times A)\times\{1,\ldots,N_i\}\times\{1,\ldots,N_{i+1}\}$, in the notation of ([Rational forms along the column chain of a word: lattices, twisted chains, the terminal map and valuations at a place](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms.PRat/)). Four conditions concern the record and the forms: (i) a unit condition on its entries and a rationality condition on the kernel maps (not expanded); (ii) $K_i(F_i)\subseteq F_{i+1}$ for every word and every $i<m$, and $K^{\mu}_i(F^{\mu}_i)\subseteq F^{\mu}_{i+1}$ for the twisted chain and twisted forms of every word and every tuple $\mu$ among $\mu_0$, $\mu_*$, $\mu_*'$ and the $\mu_w$; (iii) every group $G_{0,c}$ of stage $0$ is trivial, for the chain of every word and for the twisted chains of the same tuples. Six conditions hold for a common choice of a number of $\mathbb C_{p_w}$, of power series and of signs at each finite place $w$ (not expanded): two give the form of the power series of the record at the places above the primes of the inert and signal classes, as a series with coefficients of absolute value at most $1$ times the exponential of a pairing, after the substitution of a logarithm series; one bounds from below, at inert primes up to $X''$, the valuations of the values at the origin of products of derivative minors of such series; one asserts that these valuations are non-negative at the places not above $d$; one gives the form of the power series at the primes ramified at $d$; and one consists of ten numerical conditions on Young diagrams attached to the weights.

**(35)** Eventually at the members there is a record attached to the datum satisfying two conditions (not expanded) and the following count: with $\epsilon_C=\exp(-c_I\,r\,f\log r)$ we have $0\le\epsilon_C<1$, a positivity condition holds, and for $k\in\{0,1\}$ and every subset $S$ of a set attached to the datum and to $k$, a dimension attached to $S$ differs from a quantity $\delta(S)$ by at most $\epsilon_C\,\delta(S)$.

**(36)** There is $x_r$ such that at every member with $x\ge x_r$ and $x>x_1$ and for every stage $0\le i<m$, the matrix $\pi_{i,t_0}$ of ([Divisor rows and additive-character comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.DIV.DivisionCompatibilityDataThreeSided/)) for the row-side family of the selected record, which projects all lifted coordinates of the base level at the distinguished twist $t_0$ to the selected lifted coordinates, defines a surjective linear map.

**(37)** There is $x_0$ such that at every member with $x\ge x_0$ the following two statements hold.

(37a) Four conditions on the archimedean data of the datum (not expanded): a normalisation of scaled Haar measures; for every $\tau\in\mathcal T$, the positive number $d_\tau$ of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)) is the formal degree, for a scaled measure, of a discrete-series representation with a prescribed parameter of a unitary group of rank $2r_S+k+1$; a further condition on these formal degrees; and a condition that the volume function of the datum gives the measures of fundamental domains.

(37b) There is a choice of the data of ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)) for the datum such that, for every word $u$, the character $\chi$ of the group $U$ of the initial finite level has the following property: there is an integer $n\ge1$ with $\chi(x)^n=1$ and $\chi(x)\in\jmath(\Lambda)$ for every $x\in U$. Which of the conditions of that entry the choice is required to satisfy was not checked.

**(40)** There are real numbers $C$ and $x_0$ such that at every member with $x\ge x_0$ the following holds. For a prime $p$ and an integer $e$ let $\lambda_p(E,e)$ be the length of the localization kernel $\mathcal S_{p,e}(E)$ of ([Window condition: a bound on the Tate-Shafarevich groups of the twists Q\_l/Z\_l(-k) over auxiliary abelian fields](https://andrewodesky.com/rh/lean/UpperTheory.Top.VWin/)), formed with the algebraic closure of $E$ and the places above $p$ that the datum fixes. Suppose that $\lambda_p(E,e)$ is finite for every prime $p$ and every integer $e$ with $0<e<t$, and that $\sum_p\log p\sum_{e=1}^{t-1}\lambda_p(E,e)$ converges. Then for every $j\in\{1,\dots,m\}$, $$\sum_{w}\frac{\log\mathrm{N}\mathfrak p_w}{[\Lambda:\mathbb{Q}]}\,e_w\,\eta_{j,w}\ \le\ \dim_{\mathbb{C}}Z_j\cdot\Bigl(C\bigl(f\,m\,b\,x^{2\varepsilon}+N_c\log^2x\bigr)+\sum_p\log p\sum_{e=1}^{t-1}\lambda_p(E,e)\Bigr).$$ Here $w$ runs over the places of $\Lambda$ with $\mu_w\ne\mu_0$ in the finite set $\mathcal S$ of ([Local size and support data](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.SizeData%E2%82%82/)); $\mathfrak p_w$ is the prime ideal of $w$ and $e_w$ its ramification index over $\mathbb Q$; $\eta_{j,w}$ is the non-negative rational number of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)); $Z_j\subseteq T_{\mu_0,j}$ is the image of the adjoint of the map $\theta_{\mu_0,j}\colon T_{\mu_0,j}\to M_j$ of that entry; and $N_c=|T_2|\,k\,b\,x^{2\varepsilon}/n^2$.

*Conditions that do not involve $\mathcal{A}$.*

**(11)** Four statements of analytic number theory.

(i) There is $C_1>0$ such that for every $Q\ge 3$ and every finite set of pairs $(\chi,\rho)$, with $\chi$ a primitive Dirichlet character of modulus at most $Q$ and $\rho$ a zero of $L(s,\chi)$ with $\operatorname{Re}\rho\ge 1-1/400$ and $|\operatorname{Im}\rho|\le Q$, the sum over the set of the orders of vanishing of $L(s,\chi)$ at $\rho$ is at most $C_1Q^{1/4}$.

(ii) There is $c>0$ such that for every primitive character $\chi$ of modulus $N\ge 3$: if $L(\rho,\chi)=0$ and $\operatorname{Re}\rho\ge 1-c/\log\max(N,N|\operatorname{Im}\rho|)$, then $\chi$ is real, $\rho$ is real, the zero is simple, and it is the only zero of $L(s,\chi)$ in that region; and every zero $\rho$ of $\zeta$ with $0<\operatorname{Re}\rho<1$ has $\operatorname{Re}\rho\le 1-c/\log(|\operatorname{Im}\rho|+3)$.

(iii) There is $C>0$ such that for every primitive character $\chi$ of modulus $N$ and all real $2\le T\le u$, the set $Z_T$ of zeros of $L(s,\chi)$ with $0<\operatorname{Re}\rho<1$ and $|\operatorname{Im}\rho|<T$ is finite and, with $\psi_0(u,\chi)=\sum_{n\le u}\Lambda(n)\chi(n)$, minus $u$ if $\chi$ is trivial, and with $m_\rho$ the order of the zero $\rho$, $$\Bigl|\psi_0(u,\chi)+\sum_{\rho\in Z_T}m_\rho\frac{u^{\rho}}{\rho}\Bigr|\le C\Bigl(\frac{u\log^2(NuT)}{T}+\log(Nu)+\sum_{\rho\in Z_1}\frac{m_\rho}{|\rho|}\Bigr).$$

(iv) There is $C>0$ such that for every primitive character $\chi$ of modulus $N$ and every real $t$, the zeros of $L(s,\chi)$ with $0<\operatorname{Re}\rho<1$ and $|\operatorname{Im}\rho-t|\le 1$ are finite in number and, counted with multiplicity, number at most $C\log\bigl(N(|t|+2)\bigr)$.

**(12)** Let $D$ be a datum with $r\ge1801$ whose weight rows $B_{\tau,j}$, in the notation of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)), satisfy $16\,r^{19}\le B_{\tau,j+1}-B_{\tau,j}$ for every $\tau\in\mathcal T$ and $0\le j\le m-2$. Then every automorphic setting on $D$ satisfies the normalization conditions (d) and (e) of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)).

**(13)** ([Hypothesis: the range of a product of a finite-adelic and a discrete-series convolution operator on a unitary group is finite-dimensional](https://andrewodesky.com/rh/lean/Formalism.L2.SG.RowsDef.RowsFinDim/)).

**(15)** For every family, in $\mathcal{A}$ or not, the constants $c_{30}(c_{\mathrm{out}})$ satisfy $C_0\ge 0$ and $2(C_{YL}+1)\le A_0$.

**(16)** A bound for sums over pairs of terms, uniform in the datum. It is quantified over all real constants $C_g,c_b,C_w,c_T,C_T,C_0$ with $c_b,c_T>0$, asserts the existence of constants $C_H,C_h,C_p\ge0$ and of further thresholds, and then, for every datum $D$ with size data, every automorphic setting $X$ on $D$ with a completion $Y$ and every word $u$, under three hypotheses, bounds the sums $\sum\|v_{a_1}\|\,\|v_{a_2}\|$ over finite sets of pairs of terms for $(u,u)$ with prescribed invariants. The first and third hypotheses are hypotheses 1 and 4 of (17); the second, the invariants of a pair and the bound were not expanded.

**(17)** Hypothesis (non-generic row bound) of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)).

**(18)** For all real numbers $C_g,c_b,C_w,c_T,C_T,C_0,A$ with $c_b>0$ and $c_T>0$ there are real numbers $C_B\ge0$, $C'_0$ and $C_{l,0}$ such that for all $C'\ge C'_0$ and $C_l\ge C_{l,0}$ the following holds. Let $D$ be a datum, $S$ size data for $D$, $X$ an automorphic setting on $D$, $Y$ a completion of $X$, and $u$ a word. Suppose that the six conditions of ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)) hold for $D$; that the standing conditions for the pair $(u,u)$ with constants $(C_0;C',C_l,C_g,c_b,C_w,c_T,C_T;A)$ of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)) hold; that $(X,Y)$ satisfies the normalization conditions; and that the convergence condition for $(u,u)$ holds. Then, with $b=\exp(x^\varepsilon)$ formed from $S$, $$\Gamma_1\sum_{(a_1,a_2)\in Q_1^{\rm sc}}\operatorname{Re}\langle v_{a_1},v_{a_2}\rangle\ \le\ b^{\,C_Bm^5f}\ \frac{\delta_u(X,Y)^2}{D_\star(X)},$$ where $Q_1^{\rm sc}$ is the set of ordered pairs $(a_1,a_2)$ of terms for $(u,u)$ with the same row label, both in $\mathcal A^{\rm gen}$, with $s_0(a_1,a_2)=1$ and for which the scalar predicate of the pair holds. Automorphic settings, completions, terms, $\Gamma_1$, $\delta_u$, $D_\star$, the normalization conditions and the convergence condition are those of ([Selections of spectral realizations, sums of geometric terms and two row hypotheses](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)).

**(34)** $c_I>0$.

**(38)** Let $D$ be a datum whose volume function gives the measures of fundamental domains, in the sense of ([Normalised Haar measures on the adelic unitary groups of Hermitian spaces over the CM field, and the volume function of a datum](https://andrewodesky.com/rh/lean/Formalism.MainNotions.StandardLattice.IsVolMeas/)). Let $W$ be a Hermitian space with recorded lattice data over $E$ of rank $d\ge3$ and signature $(P,Q)$, with Hermitian form $h$. If $P\ge1$ put $s=1$ and $(P',Q')=(P-1,Q)$; if $Q\ge1$ put $s=-1$ and $(P',Q')=(P,Q-1)$. In each of these cases there are $x\in W$ with $h(x,x)=s$, a Hermitian space $W'$ with recorded lattice data over $E$ of signature $(P',Q')$, and an $E$-linear isometric map $W'\to W$ whose image is the orthogonal complement of $x$, such that $$\frac{\operatorname{vol}(W')}{\operatorname{vol}(W)}=\Bigl(\frac{(2\pi)^d}{(d-1)!}\Bigr)^{f}\bigl((2v)^{f}\bigr)^{\frac12-d}\,\frac1{L_d},\qquad v=\tfrac12\,|\operatorname{disc}E|^{1/[E:\mathbb Q]},$$ where $L_d=\prod_{\mathfrak P}\epsilon_d(\mathfrak P)$ over the maximal ideals $\mathfrak P$ of $\mathcal O_E$, with $$\epsilon_d(\mathfrak P)=\bigl(1-(-1)^d\,\mathrm N\mathfrak P^{-d/2}\bigr)^{-1}\ \text{ if }\bar{\mathfrak P}=\mathfrak P,\qquad\epsilon_d(\mathfrak P)=\bigl(1-\mathrm N\mathfrak P^{-d}\bigr)^{-1/2}\ \text{ if }\bar{\mathfrak P}\ne\mathfrak P.$$

**(39)** For every datum and every Hermitian space $W$ with recorded lattice data over $E$ of rank $2$ and signature $(2,0)$: the mass of the genus of its recorded lattice $L_0$ equals the mass of the genus of $\mathcal{O}_E^{\,2}$ for the form $\bar x_1y_1+\bar x_2y_2$.
