---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean",
  "declarations": [
    "GlobalTheory.rowNGP_of_siegelWeil"
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

## The Siegel-Weil formula implies the bound on the non-generic part of a row sum

[Theorem THETA.1.0027](https://andrewodesky.com/rh/lean/GlobalTheory.rowNGP_of_siegelWeil/)

Assume ([Hypothesis: the Siegel-Weil formula for unitary groups over a CM extension, for nondegenerate Fourier coefficients in the range M \> 2n](https://andrewodesky.com/rh/lean/HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent/)). Then for all real numbers $C_g,c_b,C_w,c_T,C_T,C_0$ with $c_b>0$ and $c_T>0$ there are a real number $C_4\ge 0$ and real numbers $C'_0$, $C_{l,0}$ such that for all $C'\ge C'_0$ and $C_l\ge C_{l,0}$ the following holds.

Let $D$ be the data of the construction, $S$ size data for $D$, $X$ an automorphic setting for $D$, $Y$ a completion of $X$, and $u,u'$ two indices of $D$ (these five notions are described below). Assume:

1. the six conditions of ([Period, measure and twist comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Ties/)) hold for $D$;
2. the standing size conditions on $(D,S)$ with constants $C',C_l,C_g,c_b,C_w,c_T,C_T,C_0$ (described below; not expanded), and $C_0\ge 1$;
3. $m\ge 4$; $T_u$ and $T_{u'}$ are primes $\ge 3$ that split completely in $E$; $g_0\ne g_1$ are primes that split completely in $E$; $\gcd(g_0g_1,\,T_uT_{u'})=1$; and $T_u\equiv T_{u'} \pmod{g_0g_1}$;
4. the normalization conditions on $(X,Y)$ (listed below);
5. $\sum_t\|\mathbf{B}(t)\|<\infty$, $\sum_t\|\mathbf{v}(t)\|<\infty$ and $\Gamma_1>0$, the sums being over the terms $t$ for $(u,u')$ defined below.

Then $$\Gamma_1\sum_{(t_1,t_2)}\mathrm{Re}\,\big⟨ \mathbf{v}(t_1),\mathbf{v}(t_2)\big⟩\;\le\;2^{-(k-m-3)}\;b^{\,C_4\,m^5 f}\cdot\frac{d_u\,d_{u'}}{D^*},$$ where the sum is over the ordered pairs of terms $t_1,t_2$ for $(u,u')$ such that $G(t_1)\ne0$, $G(t_2)\ne 0$, neither $t_1$ nor $t_2$ is generic, $t_1$ and $t_2$ lie in the same row, and $s_0(t_1,t_2)=1$.

**The data.**

- *The datum $D$* has the member identifications of ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). Use its ranks and fields from ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Write $\mathcal W$ for its finite nonempty source set and $D_*$ for its scalar in ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). For each source $u$, use its member of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), with prime $T_u$ and comparison scalar $D_u^*=D_*$. Put $V=Y_0$, the initial Hermitian space of $D$, and $f=2n$.
- *Size data $S$ for $D$* contains real numbers $x>1$ and $0<\varepsilon<1/52$, from which $b=\exp(x^{\varepsilon})$, together with further numerical data constrained by $D$.
- *An automorphic setting $X$ for $D$* fixes coordinates on $V$ and the adelic unitary group $G$, with infinite and finite factors $G_\infty,G_f$. Choose its flags and finite test vectors, and its compact source models, as in the respective conditions of ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)). Write $V_\pi(u)$ for its source Hilbert space $V_u$, $W_u:G_\infty\to V_\pi(u)$ for its source function, $F_u$ for its flag, and $K_2,\chi_2$ for its finite level and character.
- *A completion $Y$ of $X$* consists of the finite row lattices and their splittings, column representatives, rational transversals and fundamental sets, residue-field reductions and characters, and local lattice models with comparison scalars in the finite rows, columns and moments condition of ([Spectral column and period realizations](https://andrewodesky.com/rh/lean/Formalism.L2.SG.HidaSetting.HidaSetting/)). Write $R_u$ for its chosen finite set of row lattices. The residue fields here have cardinality $g_0$ or $g_1$.

**Terms.** A *term for $(u,u')$* consists of $\Lambda\in R_u$, $\Lambda'\in R_{u'}$ and a class of $E$-linear automorphisms $\gamma$ of $V$ that preserve the form, carry $\Lambda'$ to $\Lambda$, and satisfy a further condition relating $\Lambda$, the flags $F_u,F_{u'}$ and $\gamma$ (not expanded). Two such $\gamma$ are in the same class if they differ by left multiplication by an element of a set $N(\Lambda,F_u)$ of automorphisms of $V$ and right multiplication by an element of $N(\Lambda',F_{u'})$ (these sets are not expanded). Each $\gamma$ gives a point of $G$; write $\gamma_\infty$ for its component in $G_\infty$. To a term $t=(\Lambda,\Lambda',[\gamma])$ are attached:

- the operator $A(t):V_\pi(u')\to V_\pi(u)$, $$A(t)=c\,\chi(t)\int_{\Omega_t} W_u(x)\,\big⟨ W_{u'}(\gamma_\infty^{-1}x),\ \cdot\ \big⟩\,dx,$$ an integral for a measure on $G_\infty$ belonging to $X$, where $\gamma$ is a chosen representative of the class, $\Omega_t\subset G_\infty$ is a fundamental domain for the set of the $n_\infty$ with $n\in N(\Lambda,F_u)$ and $\gamma^{-1}n\gamma\in N(\Lambda',F_{u'})$, $c$ is a real constant depending on $u,u'$, and $\chi(t)$ is a complex number ($c$ and $\chi(t)$ are not expanded);
- the vector $\mathbf{v}(t)$ in the Hilbert space $\bigoplus_{(\Lambda,\Lambda')\in R_u\times R_{u'}}\mathrm{HS}(V_\pi(u'),V_\pi(u))$ of tuples of Hilbert-Schmidt operators: its component at the pair $(\Lambda,\Lambda')$ of $t$ is $\sqrt{w(\Lambda)w'(\Lambda')}\,A(t)$ and its other components are $0$, where $w(\Lambda)$ is the reciprocal of the cardinality of a set of automorphisms attached to $\Lambda$ and $F_u$ (not expanded), and $w'(\Lambda')$ likewise for $\Lambda'$ and $F_{u'}$;
- the *row* of $t$: the triple $(\Lambda,\Lambda',\iota(t))$, where $\iota(t)\in\prod_v\mathrm{GL}_k(\mathbb F_v)$ is the reduction of an element of $G_f$ determined by $t$;
- an element $G(t)\in E$ and the property of being *generic* (neither is expanded);
- an operator $\mathbf{B}(t)$, used only in condition 5 (not expanded).

For two terms with the same lattices $\Lambda,\Lambda'$, $s_0(t_1,t_2)$ is $k$ minus the dimension of an $E$-vector space determined by $\Lambda$, the flags and $\gamma_2\gamma_1^{-1}$ (not expanded); for other pairs $s_0=0$. The constant $\Gamma_1$ is the real part of $\prod_v\gamma_v$, where $\gamma_v$ is a normalized sum over $\mathrm{GL}_k(\mathbb F_v)$ formed with $\psi_v$ (not expanded). Finally $d_u$ is the complex dimension of a space of linear maps from $V_\pi(u)$ to a space of functions, and $D^*$ is a real number attached to $X$ (neither is expanded).

**The conditions.** Condition 2 is a list of inequalities between $k$, $m$, $f$, $x^{\varepsilon}$, $b$, $g_0$, $g_1$, weights and other numbers recorded in $D$ and $S$, with the eight constants as parameters; for example $C'm^5f\,x^{\varepsilon}\le k$, $m^4\le f\le k$, and $(kb)^8\le g_i\le b^{C_g}$ for $i=0,1$. Condition 4 consists of: $K_2$ contains a certain subset of $G_f$ on which $\chi_2=1$, is contained in another subset of $G_f$, and has positive finite measure; a condition on $K_2$ for each index; $d_u$ and $D^*$ equal the numbers recorded for them in $D$; a condition on $X$ involving the functions $W_u$; integrability of a function on $G_\infty$ belonging to $X$; the existence of an auxiliary object and of a nontrivial continuous unitary character of $\mathbb A_F$ trivial on $F$ that satisfy five compatibility conditions with $X$ and $D$; and an inequality for each index of $D$. None of the statements in this paragraph has been expanded beyond what is written.
