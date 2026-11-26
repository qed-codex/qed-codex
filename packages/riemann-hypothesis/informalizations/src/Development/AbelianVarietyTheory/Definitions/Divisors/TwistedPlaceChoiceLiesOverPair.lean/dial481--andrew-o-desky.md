---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/TwistedPlaceChoiceLiesOverPair.lean",
  "declarations": [
    "GlobalTheory.BigTop.Fun.GridFit",
    "GlobalTheory.BigTop.Fun.HasGrid"
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

## Grids with compatible choices over a point of a family, and their period functionals

[Definition / hypothesis THETA.D272](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.Fun.HasGrid/)

The bound for the maximal slope of the row lattice of a point is proved at the points that carry a grid of Hermitian spaces together with data from which finitely many period functionals on the row space are formed. This page defines when a point *has a grid with compatible choices*, and defines the functionals.

**Setting.** Let $p$ be a point over a member $(x,i)$ of a family, in the sense of ([Admissible points over the members of a family, the row lattice of a point and its maximal slope](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.FamHyp/)), and let $b=\exp(x^{\varepsilon})$. Let $D$ be the datum of the member. We use the notation of ([Grids of Hermitian spaces with Weil data, and properties of all grids with large parameters](https://andrewodesky.com/rh/lean/GlobalTheory.ChiGrid.GridData/)) for $D$: the CM field $E$ with its subfields $F$ and $E_0$, the ideal $\mathfrak c$ of $E_0$, the integers $k,m,f,r$ and $t_0$, the primes $g_0,g_1,p_\delta,p'_\delta$, the coefficient field $K$ with its embedding $\jmath\colon K\to\mathbb C$, and the Hermitian spaces $Y_j$ $(0\le j<m)$ and $X'$; we put $Y_m=X'$. Let $K_0\subseteq K$ be the intermediate coefficient field of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Let $\mathcal T$ be the tuple set of the point and $\mu_0\in\mathcal T$ its base tuple.

The analytic realisation data of $p$ contain the data of a family of characters for $D$ with index set $\mathcal T$, in the sense of the page on grids: the character frame with its Hecke characters $\mu^0_j$ $(0\le j<m)$, $\eta$, $\chi_\Psi$, $\delta$, $\delta'$; the Hecke characters $\xi_t$ and the finite sets of places $Q(t)$ for $t\in\mathcal T$; and the lattices with their frames. They also contain an additive character $\psi$ of $\mathbb A_F$ with a compatible family $\theta$; archimedean models attached to the spaces $Y_0,\dots,Y_m$, each with a Cartan involution and a basis at every $\tau\in\Psi$; for every $t\in\mathcal T$ and $0\le k<m$ a Weil representation $\omega_{t,k}$ for the pair $(Y_k,Y_{k+1})$ and a vacuum vector $v_k$ for this pair; the complex vector space $H_E$ in which the row theta maps of the point take their values; and, for every vector $\mathbf w$ of the archimedean model attached to $Y_0$, a linear map $u\mapsto f_{u,\mathbf w}$ from $H_E$ to the complex functions on $G_{Y_0}(\mathbb A)$. This page does not reproduce the definitions of the archimedean models and of the map $u\mapsto f_{u,\mathbf w}$.

A finite place $w$ of $K$ is *twisted* if the tuple that $D$ assigns to $w$ differs from the base tuple of $D$. At a twisted place $w$ the member carries the choices of ([Twist period lattices and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)): a twist index $i_w$ with its prime $\ell_{i_w}$, a finite set $Q_w$ of finite places of $E$, an integer $k_w$, a character $\psi'_w\colon R_{i_w,Q_w}\to O_{i_w,k_w}^{\times}$ and a coefficient embedding $\epsilon_w$ of $K$ into the fraction field of a discrete valuation ring that contains $O_{i_w,k_w}$. The point carries a Hecke character $\psi_w$ of $E$ for every finite place $w$ of $K$.

**Grids over the point.** Let $C_F$ be a real number. A *grid over $p$ with parameter $C_F$* is a grid, in the sense of the page on grids, for the data of a family of characters contained in the realisation data of $p$, with constants $(1,C_F,b)$. The definition of a grid uses these data only; the conditions that the page on grids imposes on a family of characters are not required here. Weil data on a grid are as on that page. Thus a grid has the spaces $V_{i,j}$ with $V_{0,j}=Y_j$, the spaces $C_i$, the places $S_0$, $W_0$ with the exponents $\ell(v)$ and $a(v)$, the modulus $\mathfrak m$, and the characters $\chi_i$ and $\nu_{t,i,j}$.

Weil data $\mathcal W$ on a grid over $p$ *extend the Weil data of the point* if

- the additive character and the compatible family of $\mathcal W$ are $\psi$ and $\theta$;
- for $0\le j\le m$, the Cartan involutions and the bases of $\mathcal W$ at the node $V_{0,j}=Y_j$ are those of the point;
- for every $t\in\mathcal T$ and $0\le k<m$, the Weil representation of $\mathcal W$ for the pair $(V_{0,k},V_{0,k+1})$ of the second kind for $t$ is $\omega_{t,k}$.

**Grids that fit the point.** A grid $\mathcal G$ over $p$ *fits the point* if the following seven conditions hold. For a Hecke character $\chi$ of $E$ and a finite place $v$ of $E$ at which $\chi$ is unramified, $\chi_v(\varpi_v)$ is the value of its component at $v$ on the fixed uniformizer.

(F1) For every finite place $v$ of $E$ at which the respective character is unramified, the numbers $\mu^0_{j,v}(\varpi_v)$ $(0\le j<m)$, $\chi_{\Psi,v}(\varpi_v)$, $\delta_v(\varpi_v)$, $\delta'_v(\varpi_v)$ and $\eta_v(\varpi_v)\,N(v)^{-1/2}$ lie in $\jmath(K_0)$.

(F2) For $1\le i\le m$ and every finite place $v$ of $E$ at which $\chi_i$ is unramified, $\chi_{i,v}(\varpi_v)\in\jmath(K_0)$. For every $v\in S_0$, the field $K_0$ contains a primitive root of unity of order $N(v)^{\ell(v)}$.

(F3) For every twisted place $w$, the prime $\ell_{i_w}$ is the residue characteristic of $w$, and $i_w$ lies under $w$ or under its complex conjugate $\bar w$. If $w$ and $w'$ are twisted, $w'$ has the same restriction to $K_0$ as $w$ or as $\bar w$, and $Q_w\neq\emptyset$, then $i_w=i_{w'}$. Here a twist index $i$ *lies under* a finite place $w$ of $K$ if, for every $y\in\mathcal O_{K_0}$, the image of $y$ under the embedding of $K_0$ into the fraction field of the discrete valuation ring $O^0_i$ lies in the maximal ideal of $O^0_i$ exactly when $w(y)>0$.

(F4) For every twisted place $w$: every $P\in Q_w$ satisfies $P\ne\bar P$; no place of $Q_w$ lies in the set $S_{0,i_w}$; and $\bar P\in Q_w$ for every $P\in Q_w$.

(F5) There are natural numbers $N_0(i)$, one for each twist index $i$, such that for every twisted place $w$, every integer $a$ prime to $\ell=\ell_{i_w}$ and every abelian theta label $\lambda$ of $i_w$, $$\Theta_\lambda\bigl(Q_w,(\psi'_w)^{a}\bigr)\neq0,\qquad -N_0(i_w)\ \le\ v_\ell\Bigl(\Theta_\lambda\bigl(Q_w,(\psi'_w)^{a}\bigr)\Bigr)\ \le\ c_{0,\lambda}+\ell^{-2}.$$ The sums $\Theta_\lambda(Q,\Psi)$, the numbers $c_{0,\lambda}$, the valuation $v_\ell$, the sets $S_{0,i}$ and the rings $O^0_i$, $O_{i,k}$ are those of ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)).

(F6) Let $w$ be a twisted place, let $v$ be a finite place of $E$ that does not belong to $Q_w$ and does not lie above the residue characteristic of $w$, and let $\sigma$ be a Frobenius element at $v$ in the Galois group of $E$. If $y\in K$ satisfies $\jmath(y)=\psi_{w,v}(\varpi_v)^{-1}$, then $$\epsilon_w(y)=\psi'_w\bigl(\operatorname{Art}_{i_w,Q_w}(\sigma)\bigr),$$ where $\operatorname{Art}_{i,Q}$ is the surjection of ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)).

(F7) Let $\mathfrak f'_0=(g_0g_1p_\delta p'_\delta)^2\,\mathfrak p_{v_0}$, an ideal of $\mathcal O_F$, where $\mathfrak p_{v_0}$ is the prime ideal of the place $v_0$ of the grid, and for a prime $\ell$ let $\delta_\ell$ be $\delta'$ if $\ell=p_\delta$, and $\delta$ otherwise. For every twist index $i$ that lies under a twisted place, with $\ell=\ell_i$:

(a) every finite place of $E$ that lies above a place of $F$ dividing $\mathfrak f'_0$ belongs to $S_{0,i}$;

(b) there is a ring homomorphism from $\mathbb C$ to an algebraic closure of the fraction field of $O_i$ that restricts on $\jmath(K_0)$ to the embedding of $K_0$ fixed for $i$, and for which (c) and (d) hold;

(c) every abelian theta label $\lambda$ of $i$ is the label, at some integer $s$ admissible for $\lambda$, of one of the Hecke characters $\mu^0_j\,\delta_\ell\,\chi_{a}^{-1}$ with $0\le j<m$ and $1\le a\le m$. This means: $\lambda$ has stage $j+1$; at every place $P$ outside $S_{0,i}$ the Hecke parameter of $\lambda$ is the inverse of the value of this character at the uniformizer of $P$; and there is a nonzero factor such that, for every finite set $Q$ of places that satisfies the three conditions of (F4) with $i$ in place of $i_w$, the theta coefficients of $\lambda$ on $R_{i,Q}$ are this factor times the sums, over the fibres of a reciprocity map, of the class terms of this character at $s$ for the conductor formed from $\mathfrak f'_0$ and $Q$. The comparisons are made through the homomorphism of (b), in the form that belongs to the side of $\lambda$;

(d) conversely, for all $0\le j<m$, $1\le a\le m$, each of the two sides, and every integer $s$ with $1\le s\le k+m\,(t_0+s_F+1)+1$, some abelian theta label of $i$ on that side is the label at $s$ of $\mu^0_j\,\delta_\ell\,\chi_a^{-1}$ in the sense of (c).

This page does not reproduce the definitions, used in (F7), of the abelian theta labels with their sides and Hecke parameters, of the class terms and the reciprocity map, of the conductor formed from $\mathfrak f'_0$ and $Q$, and of the integers $s$ admissible for a label. In (d), $s_F=r+6$ if $r$ is odd and $s_F=r+7$ if $r$ is even.

**Choices on a grid.** Let $\mathcal G$ be a grid over $p$ with Weil data $\mathcal W$, and let $n\ge0$ be an integer. *Choices of size $n$* on $(\mathcal G,\mathcal W)$ consist of the following nine items.

1. A system of measures $\mathfrak M$ on the grid, in the sense of ([Square constants of a grid: matched test data and normalised measures](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/)): a measure $\nu_V$ on $G_V(\mathbb A)$ and a subset $\mathfrak F_V$ for every node $V$, and a measure $\nu_N$ with a subset $\mathfrak F_N$ on the adelic points of the unipotent group $N$ attached to the orthogonal extension of $C_m$ to $V_{m,0}$.
2. For $0\le i<m$, a polynomial $\varrho_i\in\mathrm{Pol}_{p_i}$, where $p_i$ is the pair $(V_{i,0},V_{i+1,0})$ and $\mathrm{Pol}_p$ is the polynomial ring of that page.
3. A complex linear functional $\xi$ on the coefficient space $\mathcal V$ of $C_m$, a finite-dimensional complex vector space on which $G_{C_m}(\mathbb A)$ acts through its archimedean part by a representation $\varsigma$, with a $K$-form $\mathcal V_K$ that has a standard basis $(\beta_q)_{q\in\mathfrak B}$. This page does not reproduce the definition of $\mathcal V$, which depends on the weight arrays of $D$.
4. A *chain vector*: polynomials for the pairs $(Y_k,Y_{k+1})$, $0\le k<m$, and a vector of the archimedean model attached to $Y_m=X'$. The maps of the realisation data that belong to the polynomials send this vector to a vector $\mathbf w$ of the archimedean model attached to $Y_0$.
5. Archimedean matching data $\varrho^{\rm arch}$ for $\mathcal W$, in the sense of ([Square constants of a grid: matched test data and normalised measures](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/)).
6. A choice of bases and normalisations $\mathcal S$ for $(\mathcal G,\mathcal W)$, in the sense of ([Rationality hypothesis for a grid with Weil data](https://andrewodesky.com/rh/lean/GlobalTheory.RowTest.NumbersIn/)), together with a linear map from the coefficient space of the realisation data at $X'$ to a space of polynomials, subject to a compatibility condition that this page does not reproduce.
7. Class representatives. Let $K^+$ be the group of the elements of the finite part of $G_{C_m}(\mathbb A)$ that stabilise the completed lattice of $C_m$ and act trivially on it modulo $\mathfrak m$, and let $\mathrm{Cl}^+$ be the set of classes of the unitary group of $C_m$ of level $K^+$, a quotient of the finite part of $G_{C_m}(\mathbb A)$ whose equivalence relation this page does not reproduce. The item is a representative $x_c$ of every class $c\in\mathrm{Cl}^+$.
8. A bijection $e$ from $\{1,\dots,n\}$ to $\mathcal Y\times\mathrm{Cl}^+\times\mathfrak B$, where $\mathcal Y=\prod_{0\le i<m}H_i/\mathfrak mH_i$ and $H_i$ is the module of matrices that map $\Lambda(V_{i+1,0})$ into $\Lambda(V_{i,0})$, as in item 5 of the Weil data on the page on grids.
9. Complex numbers $c_{i,j}(t)$ for $0\le i,j<m$ and $t\in\mathcal T$.

**The period functionals.** Let choices of size $n$ be given, and let $1\le a\le n$ with $e(a)=(y,c,q)$, $y=(y_i)_{0\le i<m}$. For a complex function $F$ on $G_{V_{i,0}}(\mathbb A)$ put $$(\mathcal L_{i}F)(h)=\int_{\mathfrak F_{V_{i,0}}}k_{p_i}\bigl(\Phi_{p_i}(\phi_{i,y_i},\varrho_i);\,g,h\bigr)\,F(g)\,d\nu_{V_{i,0}}(g)\qquad(h\in G_{V_{i+1,0}}(\mathbb A)),$$ where $k_{p}$ is the kernel of a test function for the pair $p$ and $\phi_{i,y}$ is the function of the Weil data for the class $y$, both as on the page on grids, and $\Phi_p(\phi,P)$ is the polynomial test function of ([Square constants of a grid: matched test data and normalised measures](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/)). Let $\Psi_a$ be the function on the finite part of $G_{C_m}(\mathbb A)$ with values in $\mathcal V_K$ that is supported on the class $c$ and is given by $\Psi_a(\gamma\,x_c\,\kappa)=\varsigma_K(\gamma)\beta_q$ for $\gamma\in G_{C_m}(F)$ and $\kappa\in K^+$, where $\varsigma_K$ is the action of $G_{C_m}(F)$ on $\mathcal V_K$; when several $\gamma$ give the same element, the values are added. The identification of the finite part of $G_{C_m}(\mathbb A)$ with the group on which $\Psi_a$ is defined and the map $\mathcal V_K\to\mathcal V$ belong to the definition of the coefficient space. Put $\varphi_a(h)=\xi\bigl(\varsigma(h)^{-1}\Psi_a(h_f)\bigr)$ for $h\in G_{C_m}(\mathbb A)$ with finite part $h_f$. Let $\iota\colon G_{C_m}(\mathbb A)\to G_{V_{m,0}}(\mathbb A)$ be the embedding that belongs to the orthogonal extension of $C_m$ to $V_{m,0}$, and let $\chi_N$ be the character of $N(\mathbb A)$ formed from $\psi$ and this extension; this page does not reproduce the definition of $\chi_N$. The *period functional* $\Pi_a$ is the function on $H_E$ given by $$\Pi_a(u)=\int_{\mathfrak F_{C_m}}\int_{\mathfrak F_N}\varphi_a(h)\;\bigl(\mathcal L_{m-1}\cdots\mathcal L_{0}\,f_{u,\mathbf w}\bigr)\bigl(\upsilon\,\iota(h)\bigr)\;\overline{\chi_N(\upsilon)}\;d\nu_N(\upsilon)\,d\nu_{C_m}(h).$$ It depends on the items 1, 2, 3, 4, 7 and 8 of the choices; we write $\Pi_a^{\varrho',\xi'}$ for the functional formed with $(\varrho',\xi')$ in place of $(\varrho,\xi)$ and with the other items unchanged.

**Compatible choices.** Choices of size $n$ on $(\mathcal G,\mathcal W)$ are *compatible with the point* if the following four conditions hold.

(C1) The seven conditions:

(a) no place of any of the sets $Q(t)$, $t\in\mathcal T$, contains the integer $N(\mathfrak c)$, the norm of the ideal $\mathfrak c$;

(b) $\mathcal W$ extends the Weil data of the point;

(c) the system $\mathfrak M$ satisfies conditions 1 and 2 of a normalised system, in the sense of ([Square constants of a grid: matched test data and normalised measures](https://andrewodesky.com/rh/lean/GlobalTheory.FunObj.IsSquareConst/)), at the nodes $V_{i,0}$ $(0\le i\le m)$ and at $C_m$, where the group $K_V(t)$ of that page is, for every $t$, the group of the elements that stabilise the completed lattice of the node and act trivially on it modulo $\mathfrak m$; and $\nu_N$ is a Haar measure for which $\mathfrak F_N$ is a fundamental domain for $N(F)$ of measure $1$;

(d) for $0\le k<m$, the vacuum $v'_{0,k}$ of $\varrho^{\rm arch}$ for the pair $(V_{0,k},V_{0,k+1})$ is the vacuum vector $v_k$ of the point;

(e) the vector $\mathbf w$ of the chain vector is not zero;

(f) for all $0\le i,j<m$ and $t\in\mathcal T$, the number $c_{i,j}(t)$ is a square constant at $(t,i,j)$ for the adelic bases of $\mathcal S$ and the matching data $\varrho^{\rm arch}$, in the sense of that page;

(g) for every $u\in H_E$: if $\Pi_a(u)=0$ for all $1\le a\le n$, then $\Pi_a^{\varrho',\xi'}(u)=0$ for all $1\le a\le n$, all families of polynomials $\varrho'$ as in item 2 and all linear functionals $\xi'$ as in item 3.

(C2) For each $g\in\{g_0,g_1\}$ there are a multiplicative map $\vartheta\colon\overline{\mathbb F}_g\to\mathbb C$ that is injective on the nonzero elements and elements $\zeta_e\in\overline{\mathbb F}_g$ of order $g^{e}-1$ $(e\ge1)$ with $\zeta_{eh}^{(g^{eh}-1)/(g^{e}-1)}=\zeta_e$ for $e,h\ge1$, such that $\vartheta$ is the map prescribed by the datum at $g$ and such that, for every polynomial $F$ over $\mathbb F_g$, the central idempotent of $\mathbb C[\mathrm{GL}_r(\mathbb F_g)]$ prescribed by the datum for $F$ is $$e_F=\sum_{\chi}\frac{\chi(1)}{|\mathrm{GL}_r(\mathbb F_g)|}\sum_{h}\chi(h^{-1})\,[h],$$ the sum over the irreducible characters $\chi$ of $\mathrm{GL}_r(\mathbb F_g)$ that have label $F$. Labels are formed with $\vartheta$ and $(\zeta_e)$ as in ([Compatibility conditions for covolume points](https://andrewodesky.com/rh/lean/GlobalTheory.BigTop.PtAt.CompatibilityConditions/)).

(C3) The rationality hypothesis for $(\mathcal S,\mu_0)$ holds, in the sense of ([Rationality hypothesis for a grid with Weil data](https://andrewodesky.com/rh/lean/GlobalTheory.RowTest.NumbersIn/)).

(C4) Put $Q_0=\prod_{v\in S_0}N(v)^{a(v)}$ and $\mathfrak m_0=\prod_{v\in S_0}w(v)^{a(v)}$, and for $0\le i,j<m$ let $h_{i,j}=\bigl(\rho(i+1,j+1)+\rho(i,j)\bigr)/2$. A *norm pair with parameters $(\delta_0,\tau_0)$*, for complex numbers $\delta_0,\tau_0$, is a datum of level $Q_0$ of a kind that this page does not reproduce; it has two natural numbers $a_P\le d_P$, called its ranks here, and a *norm*, a real number defined as a sum over a set of classes. Two norm pairs $P,P'$ with the same parameters *form a bottom of the square $(i,j)$ at $\mu_0$* if the first ranks of $P$ and $P'$ are $a_1=\rho(i+1,j+1)-2\kappa_{j+1}$ and $a_2=\rho(i,j)-2\kappa_j$, their second ranks are both $a_1+a_2$, and they satisfy conditions on their characters, formed from $\mu^0_j\,\xi_{\mu_0}$, $\chi_{m-i}$, $\eta$ and $\nu_{\mu_0,i,j}$, and on their lattices and levels, formed from $\mathfrak m_0$, its complex conjugate and $a_1$; this page does not reproduce these conditions. A complex number $z$ is a *toric sum at $s$* of a Hecke character $\chi$ of $E$, for the square $(i,j)$, if two conditions hold. First, $\chi$ is unitary, its restriction to $F$ is trivial, it has a prescribed infinity type that depends on $(i,j,s)$, and at every finite place of $E$ above a place $v$ of $F$ its conductor exponent is the exponent of $v$ in $\mathfrak f_0=\prod_{v\in S_0}v^{a(v)}$. Second, $z$ is a finite sum, over the classes $q$ of a class group attached to $\mathfrak f_0$, of the values at $0$ of lattice sums of weight $2s$ attached to $q$, each divided by the value of $\chi$ at $q$ and by the $s$-th power of a norm of $q$. This page does not reproduce the infinity type, the class group, the lattice sums or the norm. The condition has two parts.

(a) Suppose that there are complex numbers $\delta_0,\tau_0$ and, for all $0\le i,j<m$, norm pairs $P_{i,j},P'_{i,j}$ with parameters $(\delta_0,\tau_0)$ that form a bottom of the square $(i,j)$ at $\mu_0$. Then there are complex numbers $\delta_0,\tau_0$ and such norm pairs for all $0\le i,j<m$ whose norms all lie in $\jmath(K)$.

(b) Let $0\le i,j<m$, let $s$ be an integer with $1\le s\le h_{i,j}$, and let $\delta^{\flat}\in\{\delta,\delta'\}$. If $z$ is a toric sum at $s$ of $\nu_{\mu_0,i,j}$ and $z'$ is a toric sum at $s$ of $\nu_{\mu_0,i,j}\,\delta^{\flat}$, both for the square $(i,j)$, then $z'/z\in\jmath(K)$.

**Points that have a grid with compatible choices.** Let $C_F$ be a real number. The point $p$ *has a grid with compatible choices at $C_F$* if there are a grid $\mathcal G$ over $p$ with parameter $C_F$ that fits the point, Weil data $\mathcal W$ on $\mathcal G$ that extend the Weil data of the point, an integer $n\ge0$, and choices of size $n$ on $(\mathcal G,\mathcal W)$ that are compatible with the point.
