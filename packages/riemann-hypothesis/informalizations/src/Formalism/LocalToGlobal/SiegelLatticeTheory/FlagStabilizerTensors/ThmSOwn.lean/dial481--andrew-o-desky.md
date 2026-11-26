---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmSOwn.lean",
  "declarations": [
    "Formalism.L2.SG.ThmSOwn.LoopRowS",
    "Formalism.L2.SG.ThmSOwn.SSel",
    "Formalism.L2.SG.ThmSOwn.SSelF"
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

## Selections of spectral realizations, sums of geometric terms and two row hypotheses

[Definition / hypothesis THETA.D261](https://andrewodesky.com/rh/lean/Formalism.L2.SG.ThmSOwn.SSelF/)

This page fixes the vocabulary for estimates of sums of geometric terms: an automorphic setting on a datum, its completions, spectral realizations, selections of spectral realizations on a class of families, the sums of term operators, and two hypotheses bounding sums over pairs of terms.

Throughout, $D$ is a datum, that is, a choice of data satisfying ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Its finite set of source words is $\mathcal W$; for $u\in\mathcal W$ the prime $T_u$ and the dimension $d_u$, the real number $D_*$, the integers $k,m,f$, $r_S=m/2-1$, the primes $g_0,g_1$ and the root discriminant $\operatorname{rd}_E$ are as in ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)). Put $g=g_0g_1$.

**Automorphic settings, completions, spectral realizations.** These three notions divide the choices and conditions of ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)) as follows.

- An *automorphic setting* $X$ on $D$ consists of the choices of Hypothesis (spectral unitary setting), Hypothesis (flags and finite test vectors), Hypothesis (compact source models) and of the first paragraph of Hypothesis (measures) of that entry, subject to the conditions stated there, with two exceptions. Four requirements of the first hypothesis are left out: $[F':\mathbb Q]=f$, the equality of the two root discriminants, and the two identities for $D_{\rm all}$ and $D_\star$. The requirement that $K_2$ be a subgroup on which $\chi_2$ is a unitary character is also left out.
- A *completion* $Y$ of $X$ consists of the requirement that $K_2$ be a subgroup of $G_f$ on which $\chi_2$ is a unitary character, and of the choices in the first three paragraphs of Hypothesis (finite rows, columns and moments): the finite sets $\mathcal R_u$ of row lattices with their decompositions, the class sets with their representatives, the transversals and fundamental sets, the residue fields with their reductions and nontrivial characters $\psi_v$, and the local lattice models with their scalars.
- A *spectral realization* of $D$ consists of an automorphic setting $X$ on $D$, a completion $Y$ of $X$, the four requirements left out above, the group isomorphism and the additive character $\psi$ of Hypothesis (measures) with the conditions on measures stated there up to and including the conditions at each finite place, and the isomorphism of moment data chosen at the end of Hypothesis (finite rows, columns and moments). It contains neither the local comparison, which is item (2) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)) and closes Hypothesis (measures), nor Hypothesis (transport to member columns).

We use the notation of that entry for a setting $X$: the group $G_\infty\times G_f$ with its Haar measures $\mu_\infty=\prod_v\mu_v$ and $\mu_f$, the fundamental set $\mathcal F$, the completed lattice $\widehat L$, the formal degrees $d_v$, the function $\varphi$ on $G_\infty$, the test function $e$, the level $K_2$ with its character $\chi_2$, the elements $x_u\in G_f$, and for each source word $u$ the space $V_u$ with its representation $\pi_u$, the function $W_u:G_\infty\to V_u$, the subgroup $S_u$ and the quotient measure $\nu_u$.

**Selections.** Let $\mathcal C$ be a class of families, in the sense of ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)). A *selection of spectral realizations on $\mathcal C$* assigns to every family $\mathrm{Fm}$ in $\mathcal C$ a real number $x_\sigma(\mathrm{Fm})$ and, to every member $(x,i)$ of $\mathrm{Fm}$ with $x>x_1$ and $x\ge x_\sigma(\mathrm{Fm})$, a spectral realization $\sigma(x,i)$ of the datum $D(x,i)$. Its setting and completion are written $X_\sigma(x,i)$ and $Y_\sigma(x,i)$.

**Terms.** Let $X$ be an automorphic setting on $D$, $Y$ a completion of $X$, and $u,u'\in\mathcal W$. A *term for $(u,u')$* is an adelic geometric lift in the sense of ([Geometric moment terms for spectral realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.TermDef.Term/)), formed with the base flags $F_u,F_{u'}$ of $X$ and the row sets $\mathcal R_u,\mathcal R_{u'}$ of $Y$: it consists of lattices $\Lambda\in\mathcal R_u$, $\Lambda'\in\mathcal R_{u'}$ and a class of pairs $(x,\gamma)$. Let $\mathcal A(u,u')$ be the set of terms for $(u,u')$. We use the following attributes of a term $a$, all defined in ([Geometric moment terms for spectral realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.TermDef.Term/)) and ([Operators and coefficients of geometric moment terms](https://andrewodesky.com/rh/lean/Formalism.L2.SG.TermOp.aTerm/)).

- The scalar $G(a)\in E$, the identity predicate and the generic predicate are those of the rational geometric term underneath $a$. Put $$\mathcal A^{\rm id}=\{a:\ a\text{ satisfies the identity predicate}\},\quad \mathcal A^{\rm gen}=\{a:\ G(a)\ne0,\ a\text{ generic}\},\quad \mathcal A^{\rm ng}=\{a:\ G(a)\ne0,\ a\text{ not generic}\}.$$
- The operator $A_a:C_{u'}\to C_u$ between the finite-dimensional Hilbert spaces $C_u=\bigoplus_\rho V_u$.
- The vector $v_a$ in the Hilbert direct sum, over the pairs $(\Lambda,\Lambda')\in\mathcal R_u\times\mathcal R_{u'}$, of the spaces of linear maps $V_{u'}\to V_u$ with the Hilbert–Schmidt inner product.
- The row label of $a$.

For two terms $a_1,a_2$ with the same pair of lattices, represented by $(x_1,\gamma_1)$ and $(x_2,\gamma_2)$, let $s_0(a_1,a_2)$ be the integer $k-\dim_E\operatorname{pr}_1T$ of ([Operators and coefficients of geometric moment terms](https://andrewodesky.com/rh/lean/Formalism.L2.SG.TermOp.aTerm/)), computed with the flags $F=F_u$, $F'=\gamma_1F_{u'}$, $F''=\gamma_2F_{u'}$ and $\beta=\gamma_2\gamma_1^{-1}$; the scalar predicate of the pair is the scalar predicate defined there for the same flags and $\beta$. For two terms with different pairs of lattices, $s_0(a_1,a_2)=0$.

**The sum $K^0$.** Linear maps $C_{u'}\to C_u$ carry the Hilbert–Schmidt norm $\|\cdot\|_{\rm HS}$. Put $$K^0_{u,u'}(X,Y)=\sum_{a\in\mathcal A^{\rm id}}A_a+\sum_{a\in\mathcal A^{\rm gen}}A_a+\sum_{a\in\mathcal A^{\rm ng}}A_a .$$

**Sums over pairs.** For each residue field $\mathbb F_v$ of $Y$, with its character $\psi_v$, let $U_k(\mathbb F_v)\subset\mathrm{GL}_k(\mathbb F_v)$ be the group of upper triangular matrices with diagonal entries $1$, let $\psi_v^U(y)=\psi_v\bigl(\sum_{i}y_{i,i+1}\bigr)$ for $y\in U_k(\mathbb F_v)$ and $\psi_v^U(y)=0$ for other $y\in\mathrm{GL}_k(\mathbb F_v)$, and put $$\gamma_v(x)=\frac1{|U_k(\mathbb F_v)|}\sum_{y\in\mathrm{GL}_k(\mathbb F_v)}\psi_v^U(yxy^{-1})\quad(x\in\mathrm{GL}_k(\mathbb F_v)),\qquad\Gamma_1=\operatorname{Re}\prod_v\gamma_v(1).$$ Since $\psi_v^U(1)=1$, this is $\Gamma_1=\prod_v|\mathrm{GL}_k(\mathbb F_v)|/|U_k(\mathbb F_v)|$. We consider three sets of ordered pairs $(a_1,a_2)$ of terms for $(u,u')$ with the same row label:

- $Q_{\ge2}$: $G(a_1)\ne0$, $G(a_2)\ne0$ and $s_0(a_1,a_2)\ge2$;
- $Q_{1}^{\rm gen}$: $a_1,a_2\in\mathcal A^{\rm gen}$, $s_0(a_1,a_2)=1$, and the scalar predicate of the pair fails;
- $Q_{1}^{\rm ng}$: $a_1,a_2\in\mathcal A^{\rm ng}$ and $s_0(a_1,a_2)=1$.

The *convergence condition for $(u,u')$* is: $\sum_{a\in\mathcal A(u,u')}\|A_a\|_{\rm HS}<\infty$, $\sum_{a\in\mathcal A(u,u')}\|v_a\|<\infty$ and $\Gamma_1>0$.

**Column spaces.** Let $H_{u,\infty}\subset G_\infty$ and $H_{u,f}\subset G_f$ be the subgroups of elements fixing the coordinates of all $e_a$, $f_a$ and of $z_u$, and let $\Gamma_u$ be the group of rational unitary elements whose images lie in $H_{u,\infty}\times H_{u,f}$. Suppose $K_2$ is a subgroup and $\chi_2$ a unitary character on it, and put $$K_u=\{h\in H_{u,f}:\ x_u^{-1}hx_u\in K_2\},\qquad\psi_u(h)=\chi_2(x_u^{-1}hx_u)\quad(h\in K_u).$$ The *column space* $\mathrm{Col}_u$ is the space of $\mathbb C$-linear maps $T$ from $V_u$ to the complex functions on $H_{u,\infty}\times H_{u,f}$ such that, for all $\xi\in V_u$ and $y\in H_{u,\infty}\times H_{u,f}$, $$(T\xi)(\gamma y)=(T\xi)(y)\ \ (\gamma\in\Gamma_u),\qquad (T\xi)(y\cdot(1,\kappa))=\psi_u(\kappa)\,(T\xi)(y)\ \ (\kappa\in K_u),\qquad \bigl(T\pi_u(h)\xi\bigr)(y)=(T\xi)(y\cdot(h,1))\ \ (h\in H_{u,\infty}).$$ Put $$\delta_u(X,Y)=\dim_{\mathbb C}\mathrm{Col}_u,\qquad D_\star(X)=\Bigl(\prod_vd_v\Bigr)\,\mu_A(\mathcal F)\,\operatorname{Re}e(1),\qquad\mu_A=\mu_\infty\times\mu_f .$$

**Normalization conditions.** A setting $X$ on $D$ with a completion $Y$ satisfies the *normalization conditions* if (a) to (g) hold.

- (a) Every $x\in G_f$ that preserves $\widehat L$ and satisfies $(x-1)\widehat L\subseteq g\widehat L$ lies in $K_2$ and has $\chi_2(x)=1$; every element of $K_2$ preserves $\widehat L$; and $0<\mu_f(K_2)<\infty$.
- (b) For every $u\in\mathcal W$: if $x\in H_{u,f}$, $\gamma\in\Gamma_u$ and $x^{-1}\gamma x\in K_u$, then $\gamma=1$.
- (c) $\delta_u(X,Y)=d_u$ for every $u\in\mathcal W$, and $D_\star(X)=D_*$.
- (d) For every $u\in\mathcal W$ there is a bounded measurable function $\alpha:G_\infty\to\mathbb C$, vanishing outside a compact set that contains $1$, such that for every $x\in G_\infty$ the function $z\mapsto\alpha(z)W_u(xz)$ is integrable and $$\int_{G_\infty}\alpha(z)\,W_u(xz)\,d\mu_\infty(z)=W_u(x);$$ moreover $$\int\|W_u(x)\|\,\Bigl(\inf_{t\in S_u}\prod_v\|(tx)_v\|_{\rm op}\Bigr)^{N_1}d\nu_u(x)<\infty,\qquad N_1=4n^2\sqrt{2\max_vq_v},$$ where $\|\cdot\|_{\rm op}$ is the operator norm of an $n\times n$ complex matrix for the Euclidean norm on $\mathbb C^n$ and $q_v$ is the number of entries $-1$ of the diagonal sign matrix $J_{\epsilon_v}$.
- (e) $\varphi$ is integrable on $G_\infty$ for $\mu_\infty$.
- (f) There are a group isomorphism and an additive character $\psi$ as in Hypothesis (measures) of ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)) that satisfy the conditions on measures stated there up to and including the conditions at each finite place; and the local comparison of item (2) of ([Three inputs for the selected off-diagonal bound](https://andrewodesky.com/rh/lean/PI.VolStabS.MassDataS.SWXS/)) holds for $D$.
- (g) For every $w\in\mathcal W$, $$1\le T_w\left(\frac{2\pi}{\operatorname{rd}_E\,g_0g_1}\right)^{m-2}.$$

For the setting and completion of a spectral realization of $D$, the first half of (f) holds with the isomorphism and the character of the realization.

**Hypothesis (non-generic row bound).** For all real numbers $C_g,c_b,C_w,c_T,C_T,C_0$ with $c_b>0$ and $c_T>0$ there are real numbers $C_4\ge0$, $C'_0$ and $C_{l,0}$ such that for all $C'\ge C'_0$ and $C_l\ge C_{l,0}$ the following holds. Let $D$ be a datum, $S$ size data for $D$, $X$ an automorphic setting on $D$, $Y$ a completion of $X$, and $u,u'\in\mathcal W$. Suppose that

1. the six conditions of ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)) hold for $D$;
2. $(D,S)$ satisfies the standing conditions with constants $(C_0;C',C_l,C_g,c_b,C_w,c_T,C_T)$ of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/));
3. the prime conditions for $(u,u')$ of that page hold;
4. $(X,Y)$ satisfies the normalization conditions;
5. the convergence condition for $(u,u')$ holds.

Then, with $b=\exp(x^\varepsilon)$ formed from $S$, $$\Gamma_1\sum_{(a_1,a_2)\in Q_1^{\rm ng}}\operatorname{Re}\langle v_{a_1},v_{a_2}\rangle\ \le\ 2^{-(k-m-3)}\,b^{\,C_4m^5f}\ \frac{\delta_u(X,Y)\,\delta_{u'}(X,Y)}{D_\star(X)} .$$

**Hypothesis (row bounds for pairs of terms along a selection).** Let $\mathcal C$ be a class of families, $\sigma$ a selection of spectral realizations on $\mathcal C$, and $C_0$ a real number. The hypothesis *with constant $C_0$* is the following statement. For every real-valued function $a$ on finite lists of real numbers, the following holds for all sufficiently constrained families $\mathrm{Fm}$ of $\mathcal C$: there is $x_0$ such that at every member $(x,i)$ of $\mathrm{Fm}$ with $x\ge x_0$, $x>x_1$ and $x\ge x_\sigma(\mathrm{Fm})$, writing $D=D(x,i)$, $X=X_\sigma(x,i)$, $Y=Y_\sigma(x,i)$, and for all source words $u,u'$ of $D$: if

1. the family standing conditions for the pair $(u,u')$ with constants $\bigl(C_0;\,a(c_{\rm out})\bigr)$ hold at $(x,i)$, in the sense of ([Standing conditions on a datum and its size data](https://andrewodesky.com/rh/lean/Formalism.MainNotions.S.StandingNumericalData/)), where $c_{\rm out}=\mathcal C_{\rm out}$ is the list of constants of the family in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)),
2. $(X,Y)$ satisfies the normalization conditions, and
3. the convergence condition for $(u,u')$ holds,

then for each of the two sets $Q=Q_{\ge2}$ and $Q=Q_1^{\rm gen}$, $$\Gamma_1\sum_{(a_1,a_2)\in Q}\bigl|\langle v_{a_1},v_{a_2}\rangle\bigr|\ \le\ \exp\!\Bigl(-\tfrac13\,kf\log k\Bigr)\ \frac{\delta_u(X,Y)\,\delta_{u'}(X,Y)}{D_\star(X)} .$$
