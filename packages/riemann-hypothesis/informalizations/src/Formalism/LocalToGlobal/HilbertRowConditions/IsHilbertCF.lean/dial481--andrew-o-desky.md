---
{
  "module": "src/Formalism/LocalToGlobal/HilbertRowConditions/IsHilbertCF.lean",
  "declarations": [
    "Formalism.L2.Rows.KsPieces"
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

## Ideal-class representatives and unramified auxiliary fields

[Definition / hypothesis ARAK.D177](https://andrewodesky.com/rh/lean/Formalism.L2.HostDatumWithTies/)

Hypothesis (ideal classes and auxiliary fields). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)), ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)) and ([Twist period lattices and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)). Write $E/F$ for the CM extension, $E_0=\mathbb Q(s_d)$ for the quadratic subfield, $K$ for the coefficient field, and $p_\delta,p'_\delta,g_0,g_1$ for the designated rational primes. For every word $u$, let $T_u$ be its specified positive rational prime. A coefficient place $w$ is active when its chosen twist label differs from the base label; let $Q_w$ be its selected finite auxiliary set of $E$-places.

Use the specified compatible embeddings of ([Linked arithmetic and theta realizations](https://andrewodesky.com/rh/lean/Formalism.L2.TiedDataSKAlt/)), $j:E\hookrightarrow\overline{\mathbb Q}$, $j_K:K\hookrightarrow\overline{\mathbb Q}$ and $\iota:\overline{\mathbb Q}\hookrightarrow\mathbb C$: their composites are the designated complex embeddings of $E,K$. Write $E^a=j(E)$ and $K^a=j_K(K)$. All auxiliary fields below are subfields of this fixed algebraic closure.

Choose primes $\mathfrak p_\delta,\mathfrak p'_\delta$ of $E_0$ above $p_\delta,p'_\delta$. For each $F$-place $v$ above $p_\delta$ choose an $E$-place $P(v)$ above $v$ whose contraction to $E_0$ is $\mathfrak p_\delta$; make the analogous choice $P'(v)$ over $p'_\delta$ with contraction $\mathfrak p'_\delta$. For all words and generator indices require $T_u\ne g_a$. No place of $Q_w$ at any active $w$ lies over any $T_u$.

Choose for every ideal class $c$ of $E_0$ a nonzero integral ideal $\mathfrak a_c$ representing it. Every $\mathfrak a_c$ is coprime to $(T_u)$ for every word $u$. At every active $w$ and every $P\in Q_w$, require $\mathfrak a_c$ not to be contained in the contraction of $P$ to $E_0$, for every $c$. Require $K^a/\mathbb Q$ to be Galois.

For finite subfields $A\subseteq L\subset\overline{\mathbb Q}$, call $L$ abelian over $A$ when every automorphism of $\overline{\mathbb Q}$ fixing $A$ preserves $L$, and the restrictions to $L$ of any two such automorphisms commute. Write $D_L=|\operatorname{disc}L|$, and let $d$ be the arithmetic discriminant parameter. Choose finite fields $H_0,R_0,M_0,M_\delta,P_0\subset\overline{\mathbb Q}$ with the following conditions.

The field $H_0$ is abelian over $\mathbb Q(\sqrt{-d})$, $$D_{H_0}=d^{[H_0:\mathbb Q]/2},$$ and contains every finite field abelian over $\mathbb Q(\sqrt{-d})$ satisfying this same discriminant identity. The field $R_0$ contains $E^a$, is abelian over $E^a$, and satisfies $$D_{R_0}\mid D_E^{[R_0:\mathbb Q]/[E:\mathbb Q]}(g_0g_1p_\delta p'_\delta)^{[R_0:\mathbb Q]}.$$ Require $H_0\subseteq M_0$ and $$[M_0:\mathbb Q]\le[H_0:\mathbb Q]\,|\mathrm{GL}_2(\mathbb Z/12\mathbb Z)|.$$ Every rational prime dividing $D_{M_0}$ divides $6d$.

There is $y\ne0$ in $\overline{\mathbb Q}$ with $y^{12}\in M_0$ and a fractional ideal $I$ of $M_0$ such that $$(y^{12})=I^{12},\qquad M_\delta=M_0(y).$$ Every rational prime dividing $D_{M_\delta}$ divides $6d$, and $M_0\subseteq M_\delta$.

Put $h=h_E$, the class number of $E$. There are finite sets $S_j\subset\overline{\mathbb Q}$ for $0\le j<m$ with $|S_j|\le\lfloor\log_2h\rfloor$, such that every $y\in S_j$ has $y^n\in E^a$ for some positive divisor $n$ of $h$, and $$P_0=E^a\,\mathbb Q(\mu_h)\,\mathbb Q\left(\bigcup_jS_j\right).$$ Require $E^a\subseteq P_0$. Every rational prime dividing $D_{P_0}$ divides $hD_E$.

Define the field $V_0$ to be generated over $\mathbb Q$ by all $x\in\overline{\mathbb Q}$ with $$\iota(x)=\chi(P)(NP)^{-s}$$ at a finite place $P$ where $\chi$ is unramified, for all the choices $$(\chi,s)=(\mu_{0,j},0)\ (0\le j<m),\quad(\eta,1/2),\quad(\delta,0),\quad(\delta',0).$$ The value $\chi(P)$ is the fixed-uniformizer value of ([Hecke characters in recursive realizations](https://andrewodesky.com/rh/lean/Formalism.L2.Host.CharFrame/)). Let $\mathcal G$ be the member's designated finite general-linear group and put $$\mathcal N=\{|\mathcal G|,\ g_0(g_0-1),\ g_1(g_1-1),\ 3^4,\ 5^4\},$$ $$K_{\rm aux}=E^a\left(\mu_n:n\in\mathcal N\right)V_0R_0M_0M_\delta P_0.$$ All products of fields denote composita inside the fixed algebraic closure.

Finally choose a finite field $H_E\subseteq K_{\rm aux}$ abelian over $E^a$, satisfying $$D_{H_E}=D_E^{[H_E:\mathbb Q]/[E:\mathbb Q]},$$ and containing every finite field abelian over $E^a$ satisfying the same identity. These displayed discriminant and maximality conditions are the precise unramified-field conditions used here.
