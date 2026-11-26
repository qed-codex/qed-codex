---
{
  "module": "src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean",
  "declarations": [
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.Datum",
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host",
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level",
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.Obj",
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.SAB",
    "ReciprocityTheory.ChartRestriction.G.Geo.Tor.TateIso"
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

## Polarized modules and unitary moduli

[Definition / hypothesis AG.D144](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)

Use a CM field $E$ and the arithmetic notation of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). Independently choose a prime $d_{\rm mod}\equiv7\pmod{16}$, elements $\rho,w\in\mathcal O_E$ and $\rho_\infty\in\mathbb C$ with $\rho^2=-d_{\rm mod}$, $2w=1+\rho$ and $\rho_\infty^2=-d_{\rm mod}$. Let $\Psi=\{\tau:E\hookrightarrow\mathbb C:\tau(\rho)=\rho_\infty\}$ and let a bar denote CM conjugation, including its restriction to $\mathcal O_E$. Assume $\mathcal O_E/\mathcal O_{E^+}$ is unramified. An integral polarized module $\Lambda$ and its signature $(p_{\rm sig},q_{\rm sig})$ are required at each natural stage of the moduli family.

Hypothesis (integral data and moduli). At each stage the integral module is finite projective over $\mathcal O_E$ and has a signature, with the following conditions imposed using that stage's module and signature. At the selected stage, its alternating form $E_\Lambda:\Lambda\times\Lambda\to\mathbb Z$ induces a bijection $\Lambda\to\operatorname{Hom}_{\mathbb Z}(\Lambda,\mathbb Z)$ and satisfies $$E_\Lambda(ax,y)=E_\Lambda(x,\bar a y).$$ Its $\mathcal O_E$-rank is $p_{\rm sig}+q_{\rm sig}$. On $\Lambda_\mathbb R=\mathbb R\otimes_\mathbb Z\Lambda$ there is a real-linear $J$ with $J^2=-1$, $E_\Lambda(Jx,Jy)=E_\Lambda(x,y)$ and $E_\Lambda(Jx,x)>0$ for $x\ne0$. For the action $A_a$ of $a\in\mathcal O_E$ on $\Lambda_\mathbb R$, put $$T(a)=\sum_{\tau\in\Psi}\{p_{\rm sig}\tau(a)+q_{\rm sig}\bar\tau(a)\}.$$ Require $JA_a=A_aJ$, $\operatorname{tr}_{\mathbb R}A_a=2\Re T(a)$ and $\operatorname{tr}_{\mathbb R}(JA_a)=-2\Im T(a)$. These conditions define every integral polarized module of a specified signature used here.

The moduli problem parametrizes proper commutative semiabelian families with $\mathcal O_E$-action and a relatively ample rigidified symmetric cubical line bundle $\mathscr P$. The polarization has trivial translation kernel: if $t_x^*\mathscr P\otimes\mathscr P^{-1}$ is locally trivial over the base, then $x=0$. Write $\mathscr B(x,y)=\mathscr P_{x+y}\otimes\mathscr P_x^{-1}\otimes\mathscr P_y^{-1}\otimes\mathscr P_0$ for the bilinear bundle associated with $\mathscr P$. Require $\mathscr B(ax,y)\simeq\mathscr B(x,\bar a y)$ and $\mathscr P_x\simeq\mathscr B(x,wx)$. At every algebraically closed point the tangent multiplicity is $p_{\rm sig}$ at embeddings in $\Psi$ and $q_{\rm sig}$ at the others. There are compatible $\mathcal O_E$-linear identifications $\Lambda/n\Lambda\simeq A_y[n]$ for all positive integers $n$, where $A_y$ is the abelian variety at the point, with compatible primitive roots of unity, under which the Weil pairing is the root raised to $E_\Lambda(a,b)$. The root at the auxiliary level $A$ is the chosen $\zeta_A=\exp(2\pi\mathrm i/A)$. The two additive level maps agree with these identifications at levels $M$ and $A$; the first agreement is required on $\bar{\mathfrak b}\Lambda$ and its kernel contains $\mathfrak b\Lambda$, while the auxiliary map kills $A\Lambda$.

The moduli schemes are smooth and quasi-projective of dimension $\lfloor[E:\mathbb Q]/2\rfloor p_{\rm sig}q_{\rm sig}$ over $\mathbb Q(\rho_\infty,\zeta_A)$, where $\zeta_n=\exp(2\pi\mathrm i/n)$. They carry universal objects, and every such object over a reduced scheme is induced by a unique map to the moduli scheme. If an object over the dual numbers is induced both by a point and by its constant reduction, that point is constant.

## Coefficient fields and deeper moduli levels

[Definition / hypothesis AG.D143](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)

Use the polarized modules, moduli schemes and notation in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)). The original level is a triple $(M,\mathfrak b,A)$. Let $K_0\subset\mathbb C$ be the original coefficient number field, containing every image of $E$, and identify the coefficient ring of the automorphic forms with $\mathcal O_{K_0}$. For a fixed stage choose a finite extension $K_0\subseteq K\subset\mathbb C$ and a moduli scheme $X/K$ at a deeper level, together with its map to the original moduli scheme and a Cartesian map of universal semiabelian families. Write $e_{\rm lev}\ge0$ for the level exponent and $o\in\mathbb R$ for the field-size bound.

Hypothesis (level and coefficient fields). Let the deeper level be $(M_2,\mathfrak b_2,A_2)$. The level multiplier is $15^{e_{\rm lev}}$, $$M_2=M15^{e_{\rm lev}},\quad (15^{e_{\rm lev}},M)=1,\quad \mathfrak b_2=\mathfrak b I,\quad I+\bar I=\mathcal O_E,\quad A_2=1,$$ and level divisibility means $M\mid M_2$, $\mathfrak b_2\subseteq\mathfrak b$ and $A\mid A_2$. At the original level require $M$ odd and at least three, $A>0$, $\mathfrak b\bar{\mathfrak b}=(M)$, $\mathfrak b+\bar{\mathfrak b}=\mathcal O_E$, and $\mathfrak b$ generated by its elements in $\mathbb Z[w]$; impose the same conditions on the deeper triple. The field $K_0$ contains $\rho_\infty$ and the chosen primitive $\operatorname{lcm}(M,A)$th root $\zeta_{\operatorname{lcm}(M,A)}$; $K$ contains $\rho_\infty$, every image of $E$ and $\zeta_{M_2}$. The map of universal semiabelian families is Cartesian and preserves the $\mathcal O_E$-action and cubical polarization data. It carries the $15^{e_{\rm lev}}$th powers of the deeper $M_2$-level sections to the original $M$-level sections, and carries the $(A_2/A)$th powers of the auxiliary sections to the original ones. Every framed point over an algebraically closed compatible coefficient extension lifts through this map, preserving its underlying point, tangent frame, polarization line bundle, rigidification and generating section. The chosen weight-zero scalar section of the deeper model is regular and nowhere zero on these framed points. Every automorphism of $\mathbb C$ fixing $K_0$ maps $K$ into itself, and $$\log[K:\mathbb Q]+\frac{\log|\operatorname{disc}K|}{[K:\mathbb Q]}\le o.$$ For each irreducible component $Z$, put $m_\tau=p_{\rm sig}$ for $\tau\in\Psi$ and $m_\tau=q_{\rm sig}$ otherwise. Require that $K$ be algebraically closed in $$K(Z)(t_{\tau,i,j}:\tau:E\hookrightarrow\mathbb C,\ 0\le i<j<m_\tau),$$ where $K(Z)$ is the function field of $Z$ and the $t_{\tau,i,j}$ are independent variables.

A framed point means a moduli point, a basis of each tangent eigenspace and a generator of the polarization's section module. Over a commutative coefficient algebra $R$, a triangular change fixes the moduli point and replaces its tangent bases, for every embedding $\tau$ and $0\le i<m_\tau$, by $$u'_{\tau,i}=\sum_{j=0}^i g_{\tau,ij}u_{\tau,j},\qquad g_{\tau,ij}\in R,\quad g_{\tau,ii}\in R^\times.$$ Using the induced identification of the polarization line bundles, it replaces the generating section $s$ by $a s$ for a unit $a\in R^\times$.

The auxiliary theta data include the following arbitrary operation. For every commutative $K$-algebra $R$, framed point $y$ over $R$, integer $h$, section $s$ of $\mathscr P_y^{\otimes h}$ on the family over $y$, and finitely supported multiindex $\alpha:\{(\tau,i):0\le i<m_\tau\}\to\mathbb Z_{\ge0}$, choose a value $N_y(h,s,\alpha)\in R$. No linearity or naturality condition is imposed on this operation here. There is also a function $\phi_\delta:(\Lambda/\mathfrak b_2\Lambda)^0\to K$; its domain is the singleton consisting of the empty tuple. For any coefficient algebra over the level's base field, every positive integer is a unit, the distinguished square root of $-d_{\rm mod}$ is the image of $\rho_\infty$, and the distinguished primitive $A$th root is the image of $\exp(2\pi\mathrm i/A)$.
