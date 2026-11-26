---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/IsLatBasisHtLatIffSpanEq.lean",
  "declarations": [
    "GlobalTheory.CompHt.IsHTChange",
    "GlobalTheory.CompHt.IsHTFrame",
    "GlobalTheory.CompHt.IsHTFrameCp",
    "GlobalTheory.CompHt.IsLatBasis",
    "GlobalTheory.CompHt.LieTie",
    "GlobalTheory.CompHt.PointOver",
    "GlobalTheory.CompHt.htLat",
    "GlobalTheory.CompHt.htPrimes",
    "GlobalTheory.CompHt.htValSet",
    "GlobalTheory.CompHt.mixVals",
    "GlobalTheory.CompHt.val_vw"
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

## Volume slopes of the components of a unitary moduli scheme

[Definition / hypothesis ARAK.D013](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.compVolSlope/)

The volume slope of an irreducible component of a unitary moduli scheme measures the number of integral cusp forms of small norm on that component, in the weights $hu$ for a fixed weight $u$, as $h\to\infty$. It is formed from a module of integral cusp forms, a set of small forms in each degree $h$, a volume and a degree.

**Setting.** Let $X$ be a unitary moduli scheme for a CM field $E$, of signature $(p,q)$ and level $(M,\mathfrak b,A)$, with coefficient number field $K\subset\mathbb C$. Suppose that complex uniformizations of $X$ are given at every embedding $\sigma:K\hookrightarrow\mathbb C$: a finite collection of Hermitian lattice domains $\mathcal D_c$, each with a uniformizing map from $\mathcal D_c$ to the complex framed points of $X$. These objects and the notation are those of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)), ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)) and ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)), with $p=p_{\rm sig}$ and $q=q_{\rm sig}$; in particular $\Psi$ is the CM type and $\rho_\infty\in K$ is the chosen complex square root of $-d_{\rm mod}$. Put $$N=p+q,\qquad D_f=|\Psi|\binom N2,\qquad M'=\operatorname{lcm}(M,A),\qquad d_K=[K:\mathbb Q].$$ Let $X_K$ be the base change of $X$ to $K$, and let $Z$ be an irreducible component of $X_K$. Fix a real number $B$, called the cutoff, a real number $x$ and an integral weight $u\in\mathbb Z^{\Psi\times\{0,\ldots,N-1\}}$.

**Integral cusp forms.** For an integral weight $v$, let $S_Z(v,0)$ be the $K$-vector space of cusp forms of weight $(v,0)$ supported on $Z$, as defined in ([Cusp spaces and integral lattices on level covers](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.Weight/)) for $X$, $K$ and the given uniformizations. Its elements are scalar rules on the framed points of $X$. Let $\mathcal R$ be the ordinary integral-evaluation family of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)) and let $\mathcal H$ be the family of ([Hodge–Tate frames and finite-place evaluations](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.PointOver/)), both formed for $X$ and $K$. For a finite prime $\lambda$ of $K$ with residue characteristic $\ell$, put $$\mathcal V^B_\lambda=\begin{cases} \mathcal H_\lambda,&\ell\le B\text{ or }\ell\mid2\operatorname{disc}(E)M',\\ \mathcal R_\lambda,&\text{otherwise}. \end{cases}$$ This is the primewise selection of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)) for the families $\mathcal H$ and $\mathcal R$ and the selected-prime set of $E$, $M'$ and $B$. The module of $B$-integral cusp forms of weight $v$ on $Z$ is the associated integral $\mathcal O_K$-submodule $$\Lambda_{Z,B}(v)=\Lambda(S_Z(v,0);\mathcal V^B)=\{f\in S_Z(v,0):w(f)\ge0\text{ for every }\lambda\text{ and every }w\in\mathcal V^B_\lambda\}.$$

**Small forms.** An embedding $\sigma:K\hookrightarrow\mathbb C$ is permitted if $\sigma(\rho_\infty)=\rho_\infty$. For a permitted embedding $\sigma$, a frame over $Z$ is a pair $(c,z)$ of a domain label $c$ and a point $z\in\mathcal D_c$ such that the point of $X_K$ determined by $\sigma$ and by the image of $z$ under the uniformizing map of $\mathcal D_c$ lies in $Z$. For $f\in S_Z(v,0)$, write $N_{x,\sigma,c,v}(f,z)$ for the homogeneous norm of ([Homogeneous norms on unitary frame domains](https://andrewodesky.com/rh/lean/GlobalTheory.AllWt.homN/)) of the analytic reading of $f$ on $\mathcal D_c$. For $h\in\mathbb N$ and $t\in\mathbb R$, the set of small forms of degree $h$ is $$\mathcal A_{Z,h}(u,t)=\{f\in\Lambda_{Z,B}(hu):N_{x,\sigma,c,hu}(f,z)\le e^{ht}\text{ for every permitted }\sigma\text{ and every frame }(c,z)\text{ over }Z\}.$$

**Volume, degree and slope.** The volume of $Z$ at the weight $u$ is the function of $t\in\mathbb R$ $$V_{Z,B}(u,t)=\limsup_{h\to\infty}\frac{D_f!\,\log\#\mathcal A_{Z,8h}(u,t)}{d_K\,(8h)^{D_f+1}}\in[0,+\infty],$$ where $\log\#\mathcal A$ is the logarithm of the cardinality of $\mathcal A$ if the set $\mathcal A$ is finite and nonempty, $0$ if $\mathcal A$ is empty, and $+\infty$ if $\mathcal A$ is infinite. It is the volume of ([Asymptotic growth, volume and slope of graded sections](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.growth/)) for the sets $\mathcal A_{Z,h}(u,t)$, with dimension parameter $D_f$, coefficient degree $d_K$ and sampling integer $8$.

The degree $\delta_Z(u)$ of $Z$ at the weight $u$ is the real degree of the same page for the spaces $S(v)=S_Z(v,0)$ and the parameters $\Psi$ and $N$. Explicitly, let $v^{\rm std}$ be the weight with $v^{\rm std}_{\tau i}=N-1-i$, and let $$G_Z=\limsup_{h\to\infty}\frac{D_f!\,\dim_KS_Z(hv^{\rm std},0)}{h^{D_f}}\in[0,+\infty],$$ where an infinite dimension counts as $+\infty$. Then $$\delta_Z(u)=\gamma_Z\prod_{\tau\in\Psi}\ \prod_{0\le i<j<N}(u_{\tau i}-u_{\tau j}),\qquad \gamma_Z=\frac{G_Z}{\prod_{\tau\in\Psi}\prod_{0\le i<j<N}(j-i)},$$ with $G_Z$ replaced by $0$ if it is $+\infty$.

The volume slope of $Z$ at the weight $u$ is $$\operatorname{sl}_{Z,B}(u)=\inf_{t\in\mathbb R}\left(\frac{V_{Z,B}(u,t)}{\max(\delta_Z(u),0)}-t\right)\in[-\infty,+\infty],$$ the slope $s_{\delta_Z(u)}\bigl(V_{Z,B}(u,\cdot)\bigr)$ of ([Asymptotic growth, volume and slope of graded sections](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.growth/)). It depends on $x$ through the homogeneous norms.

If $\delta_Z(u)>0$, a real number $a$ satisfies $a\le\operatorname{sl}_{Z,B}(u)$ if and only if $$V_{Z,B}(u,t)\ge\delta_Z(u)\,(a+t)\qquad\text{for every }t\in\mathbb R.$$

## Eigenspace submodules and integral frames

[Definition / hypothesis AV.D024](https://andrewodesky.com/rh/lean/GlobalTheory.EigenSplit.eigenSub/)

An action on a vector space gives eigenspace intersections and, when the coefficient algebra splits, projected submodules. Integral frames describe a submodule within the span of chosen vectors.

**Eigenspace intersections.** Let $O$ and $\Lambda$ be commutative rings, let $C$ be a field with a specified homomorphism $\iota:O\to C$, and let $V$ be a $C$-vector space, viewed as an $O$-module through this homomorphism. Fix a ring homomorphism $\rho:\Lambda\to\operatorname{End}_C(V)$ and an $O$-submodule $X\subseteq V$. For a ring homomorphism $\chi:\Lambda\to C$, put $$V_\chi=\{x\in V:\rho(a)x=\chi(a)x\text{ for every }a\in\Lambda\},\qquad X^{\mathrm{sub}}_\chi=X\cap V_\chi.$$

**Projected submodules.** Let $I$ be an index set and let $\sigma_i:\Lambda\to C$, for $i\in I$, be ring homomorphisms such that $$\alpha:C\otimes_{\mathbb Z}\Lambda\longrightarrow C^I,\qquad \alpha(c\otimes a)_i=c\sigma_i(a),$$ is bijective. Here $C^I$ is the algebra of all functions $I\to C$, with pointwise operations. For each $i$, let $e_i$ be the inverse image under $\alpha$ of the function equal to $1$ at $i$ and $0$ elsewhere. Extend $\rho$ to the $C$-algebra homomorphism $$\widetilde\rho:C\otimes_{\mathbb Z}\Lambda\longrightarrow\operatorname{End}_C(V),\qquad \widetilde\rho(c\otimes a)(x)=c\rho(a)x.$$ The eigenspace projection and projected submodule at $i$ are $$\pi_i=\widetilde\rho(e_i),\qquad X^{\mathrm{quot}}_i=\pi_i(X)=\{\pi_i(x):x\in X\}.$$

**Integral frames.** For an $O$-submodule $Y\subseteq V$ and a finite tuple $w_1,\ldots,w_n\in V$, the integral-frame condition is that the vectors are $C$-linearly independent and $$\sum_{i=1}^n Ow_i=Y\cap\operatorname{span}_C\{w_1,\ldots,w_n\}.$$ For the empty tuple, both spans are zero.

**Scalar-extension submodules.** Let $p$ be a rational prime, suppose $O$ is a $\mathbb Z_p$-algebra, and suppose the map $O\to C$ respects the $\mathbb Z_p$-algebra structures. For a $\mathbb Z_p$-module $T$ with an action $\Lambda\to\operatorname{End}_{\mathbb Z_p}(T)$, set $$V=C\otimes_{\mathbb Z_p}T,\qquad X=\operatorname{im}\left(O\otimes_{\mathbb Z_p}T\longrightarrow V\right),\qquad o\otimes t\longmapsto \iota(o)\otimes t,$$ The induced action on $V$ is $\rho(a)(c\otimes t)=c\otimes at$. Its eigenspace intersections and projected submodules have the definitions above.

## Finite-place valuation families and integral submodules

[Definition / hypothesis ARAK.D032](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)

These definitions turn families of finite-place evaluations into integral submodules.

**Valuation families.** Let $K$ be a number field, let $\mathcal F$ be a commutative $K$-algebra, and write $v_\lambda$ for the integer valuation at a finite prime $\lambda$ of $K$. A function $v:\mathcal F\to\mathbb R\cup\{+\infty\}$ has the required valuation properties at $\lambda$ if, for every $f,g\in\mathcal F$ and $a\in K^\times$, $$v(0)=+\infty,\qquad v(f+g)\ge\min(v(f),v(g)),\qquad v(fg)=v(f)+v(g),$$ $$v(af)=v_\lambda(a)+v(f).$$ The function constantly equal to $+\infty$ is allowed. A family $\mathcal V$ chooses, for each $\lambda$, a possibly empty set $\mathcal V_\lambda$ of such functions. For a $K$-vector subspace $W\subseteq\mathcal F$, its associated integral $\mathcal O_K$-submodule is $$\Lambda(W;\mathcal V)=\{f\in W:v(f)\ge0\text{ for every }\lambda\text{ and every }v\in\mathcal V_\lambda\}.$$

**Ordinary integral evaluations.** Take a moduli scheme $X$ and coefficient number field $K\subset\mathbb C$ with the moduli and coefficient-field choices of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) and ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)). Use the integral-framed-point definition and fixed-presentation evaluation of ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)), with $(X,K)$ in place of the original $(X_j,K_0)$. Here $\mathcal F$ is the $K$-algebra of scalar rules, with pointwise operations.

For each $\lambda$, range over all characteristic-zero complete DVRs $R$ with finite residue field, fraction fields $L$, embeddings $\iota:K\hookrightarrow L$, positive integers $e$ such that $$v_R(\iota(a))=e\,v_\lambda(a)\qquad(a\in K^\times),$$ and integral framed points $y$ over $(R,L,\iota)$. The ordinary family $\mathcal R_\lambda$ consists of all functions $$f\longmapsto v_{R,e}(f(y)),$$ where $v_{R,e}$ is the normalized extended evaluation valuation in ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)). In particular, a zero evaluation has value $+\infty$.

**Primewise selection.** Given two families $\mathcal V',\mathcal V''$ and a set $S\subseteq\mathbb N$, define $$\mathcal V^S_\lambda=\begin{cases} \mathcal V'_\lambda,&\text{some }n\in S\text{ has image in }\lambda,\\ \mathcal V''_\lambda,&\text{otherwise}. \end{cases}$$ For a set of rational primes $S$, the first case means that the residue characteristic of $\lambda$ belongs to $S$.

For a number field $E$, a positive integer $M'$ and a real $B$, the selected-prime set is $$S_B(E,M')=\{\ell:\ell\text{ is prime and }(\ell\le B\text{ or }\ell\mid2|\operatorname{disc}E|M')\}.$$ For a level $(M,\mathfrak b,A)$ of ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)), use $M'=\operatorname{lcm}(M,A)$.

## Hodge–Tate frames and finite-place evaluations

[Definition / hypothesis PHT.D042](https://andrewodesky.com/rh/lean/GlobalTheory.CompHt.PointOver/)

Hodge–Tate frames impose an integral-frame condition on comparison vectors. Evaluating scalar rules at these frames gives a family at each finite place.

**Moduli and eigenlattices.** Fix a moduli scheme $X$, coefficient number field $K\subset\mathbb C$, universal semiabelian family $\mathscr A\to X$ and its line bundle $\mathscr P$, with the notation of ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)) and ([Coefficient fields and deeper moduli levels](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Level/)). Write $E$ for the CM field, $\Psi$ for the chosen CM type, $\tau_K:E\hookrightarrow K$ for the distinguished lift of $\tau:E\hookrightarrow\mathbb C$, and $m_\tau$ for the tangent multiplicity at $\tau$.

Fix a rational prime $p$ and an embedding $\kappa:K\hookrightarrow C=\mathbb C_p$, and put $O=\mathcal O_{\mathbb C_p}$. Use a choice of the auxiliary models $A,G,G^{\mathrm t}$, line bundle $L$, Tate module $T$, vector space $V$ and comparison map $b:\operatorname{Lie}_O(G^{\mathrm t})\to V$ of ([Auxiliary semiabelian models and Hodge–Tate comparison vectors](https://andrewodesky.com/rh/lean/GlobalTheory.HTLat.Point/)), with $\Lambda=\mathcal O_E$ and CM conjugation. Let $\eta:A\to G$ be the generic-fibre comparison followed by the map to $G$.

Let $Q\subseteq V$ be the image of $O\otimes_{\mathbb Z_p}T$ in $V$. Use the eigenspace intersections and projections of ([Eigenspace submodules and integral frames](https://andrewodesky.com/rh/lean/GlobalTheory.EigenSplit.eigenSub/)), with the splitting indexed by all embeddings $E\hookrightarrow C$. Put $\chi_\tau=(\kappa\circ\tau_K)|_{\mathcal O_E}$ and $$Y_\tau=\begin{cases}Q^{\mathrm{quot}}_{\chi_\tau},&\tau\in\Psi,\\Q^{\mathrm{sub}}_{\chi_\tau},&\tau\notin\Psi.\end{cases}$$

**Comparison with an integral point.** Let $R$ be a characteristic-zero complete DVR with fraction field $F$, let $\iota:K\hookrightarrow F$, and let $y_0$ be an integral framed point over $(R,F,\iota)$ in ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)). Write $x_0:\operatorname{Spec}F\to X$ for its underlying point. Choose an embedding $k:F\hookrightarrow C$ with $k\iota=\kappa$, a homomorphism $k_O:R\to O$ compatible with $k$, and a map $\psi:A\to\mathscr A$.

The required comparison with $x_0$ is the existence of the following data. There are commutative semiabelian schemes $\mathcal G/R$ and $\mathcal B/F$, each with an $\mathcal O_E$-action and a rigidified symmetric cubical line bundle satisfying the adjointness and $w$-polarization identities in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)). The symmetry isomorphism preserves the rigidification. There are Cartesian maps $$m_1:\mathcal B\longrightarrow\mathscr A\text{ over }x_0,\qquad m_2:\mathcal B\longrightarrow\mathcal G\text{ over }\operatorname{Spec}F\to\operatorname{Spec}R,$$ preserving the group law, action, rigidification and cubical line data, in the sense of the maps defined in ([Polarized modules and unitary moduli](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.Geo.Tor.Host/)). There are also Cartesian group maps $$\pi:G\longrightarrow\mathcal G\text{ over }\operatorname{Spec}O\to\operatorname{Spec}R,\qquad \phi:A\longrightarrow\mathcal B\text{ over }\operatorname{Spec}C\to\operatorname{Spec}F,$$ such that $\pi$ commutes with the $\mathcal O_E$-actions and $$m_2\circ\phi=\pi\circ\eta,\qquad m_1\circ\phi=\psi,\qquad L\simeq\psi^*\mathscr P.$$ Here a Cartesian group map identifies the group in its domain with the base change of the group in its codomain.

Say that $x\in\operatorname{Lie}_O(G^{\mathrm t})$ and a dual-number point $u:\operatorname{Spec}(C[\epsilon]/(\epsilon^2))\to\mathscr A$ satisfy the tangent comparison if there exist $x_G\in\operatorname{Lie}_O(G)$ and a point $\widetilde u\in A(C[\epsilon]/(\epsilon^2))$ such that $x$ and $x_G$, viewed over $O[\epsilon]/(\epsilon^2)$, correspond modulo $p^r$ for every $r\ge0$ under the formal comparisons of ([Auxiliary semiabelian models and Hodge–Tate comparison vectors](https://andrewodesky.com/rh/lean/GlobalTheory.HTLat.Point/)), and $$\psi(\widetilde u)=u,\qquad \eta(\widetilde u)=(x_G)_C.$$

**The frame condition.** Let $z$ be the scalar extension of $y_0$ along $k$, including its tangent bases and generating section. Write these as $u^z_{\tau,j}$ and $s_z$. A framed point $y$ over $C$, with tangent bases $u^y_{\tau,i}$ and generating section $s_y$, satisfies the Hodge–Tate frame condition relative to these choices if it descends from a framed point over some reduced finite-type presentation $K[t_1,\ldots,t_s]/I$, with $I$ radical, and if there are matrices $g_\tau\in M_{m_\tau}(C)$, a scalar $a\in C$ and vectors $x_{\tau,j}\in\operatorname{Lie}_O(G^{\mathrm t})$ with the following properties.

The points underlying $y$ and $z$ agree, and, using that identification of their fibres, $$u^y_{\tau,i}=\sum_{j=0}^{m_\tau-1}g_{\tau,ij}u^z_{\tau,j},\qquad s_y=a s_z,\qquad g_{\tau,ij}=0\ (i<j),\qquad |a|_p=1.$$ The tangent comparison above holds between $x_{\tau,j}$ and $u^z_{\tau,j}$ for every $\tau,j$. Define $$w_{\tau,i}=\sum_{j=0}^{m_\tau-1}g_{\tau,ij}b(x_{\tau,j}).$$ For every $\tau$, these vectors are $C$-linearly independent and satisfy $$\sum_{i=0}^{m_\tau-1}O w_{\tau,i}=Y_\tau\cap\operatorname{span}_C\{w_{\tau,i}:0\le i<m_\tau\}.$$ For multiplicity zero, both spans are zero. The descent requirement uses the coefficient embedding $\kappa$ and the scalar-extension notion of ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)).

**The evaluation family.** Let $\lambda$ be a finite prime of $K$, and write $v_\lambda$ for its integer valuation. Range over all primes $p$, embeddings $\kappa:K\hookrightarrow\mathbb C_p$, characteristic-zero complete DVRs $R$ with finite residue field, fraction fields $F$, embeddings $\iota:K\hookrightarrow F$, and positive integers $e$ such that $$v_R(\iota(c))=e\,v_\lambda(c)\qquad(c\in K^\times).$$ Range also over all integral framed points $y_0$ over $(R,F,\iota)$, embeddings $k:F\hookrightarrow\mathbb C_p$ with $k\iota=\kappa$, and framed points $y$ over $\mathbb C_p$ for which there are a choice of the auxiliary models and comparison map above, a homomorphism $k_O$ and a map $\psi$ such that the required comparison with $x_0$ holds and $y$ satisfies the Hodge–Tate frame condition relative to these choices. The family $\mathcal H_\lambda$ consists of all functions on scalar rules given by $$f\longmapsto\begin{cases} +\infty,&f(y)=0,\\ v_\lambda(p)\,\dfrac{\log|f(y)|_p}{\log|p|_p},&f(y)\ne0. \end{cases}$$ Use the fixed-presentation evaluation $f(y)$ of ([Integral evaluation of moduli sections](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM.evalWD/)). These families have the valuation properties of ([Finite-place valuation families and integral submodules](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.IsVal/)).
