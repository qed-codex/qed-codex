---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/IsInertiaInfiniteCyclotomic.lean",
  "declarations": [
    "UpperTheory.V.Loc.Dat3",
    "UpperTheory.V.Loc.Dat3.It"
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

## Deformation rings of a sum of three characters with a sign character

[Definition / hypothesis AGR.D096](https://andrewodesky.com/rh/lean/UpperTheory.V.U3.GG/)

The theorem ([Selmer lengths and trace congruences](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)) concerns a character $\Psi$ of $\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)$ and an imaginary quadratic field $K$. Its proof deforms the sum $\Psi\oplus1\oplus\Psi^{-1}$, regarded as a homomorphism to a group $\mathcal G_3=\mathrm{GL}_3\rtimes\{\pm1\}$ whose second component is the quadratic character of $K$. This page defines the group, the deformation rings, and the points of these rings to which the hypotheses of the theorem refer.

**The group $\mathcal G_3$.** Let $R$ be a commutative ring and let $J\in\mathrm{GL}_3(R)$ be the matrix with entries $1$ on the antidiagonal and $0$ elsewhere. The map $\theta(g)=J\,{}^tg^{-1}J$ is an automorphism of $\mathrm{GL}_3(R)$ of order two, and $$\mathcal G_3(R)=\mathrm{GL}_3(R)\rtimes\{\pm1\}$$ is the semidirect product in which $-1$ acts on $\mathrm{GL}_3(R)$ by $\theta$: the product is $(g,s)(h,t)=(g\cdot{}^sh,\,st)$ with ${}^1h=h$ and ${}^{-1}h=\theta(h)$. A homomorphism of rings $f:R\to R'$ induces a homomorphism $\mathcal G_3(R)\to\mathcal G_3(R')$, by which a homomorphism $r:\Gamma\to\mathcal G_3(R)$ from a group $\Gamma$ gives $f\circ r:\Gamma\to\mathcal G_3(R')$.

For a homomorphism $r:\Gamma\to\mathcal G_3(R)$ write $r(\gamma)=(\dot r(\gamma),\nu(\gamma))$. The map $\nu:\Gamma\to\{\pm1\}$ is a homomorphism, called the *sign* of $r$, and $\dot r:\Gamma\to\mathrm{GL}_3(R)$ restricts to a homomorphism on $\ker\nu$. The entry in row $a$ and column $b$ of a $3\times3$ matrix has *weight* $b-a$. The *adjoint action* of $\Gamma$ on $M_3(R)$ defined by $r$ is $$\gamma\cdot X=\begin{cases}\dot r(\gamma)\,X\,\dot r(\gamma)^{-1},&\nu(\gamma)=1,\\ -\dot r(\gamma)\,J\,{}^tX\,J\,\dot r(\gamma)^{-1},&\nu(\gamma)=-1;\end{cases}$$ it is denoted $\operatorname{ad}r$.

For homomorphisms $\eta:\Gamma\to\{\pm1\}$ and $\Psi:\Gamma\to R^\times$, the automorphism $\theta$ fixes the matrices $\operatorname{diag}(t,1,t^{-1})$, so that $$r_{\eta,\Psi}(\gamma)=\bigl(\operatorname{diag}(\Psi(\gamma),1,\Psi(\gamma)^{-1}),\ \eta(\gamma)\bigr)$$ is a homomorphism $\Gamma\to\mathcal G_3(R)$ with sign $\eta$.

**Lifts and universal lifts.** Let $\mathcal O$ be a complete discrete valuation ring with maximal ideal $\mathfrak m_{\mathcal O}$ and residue field $k$. Let $\mathcal C_{\mathcal O}$ be the class of complete Noetherian local $\mathcal O$-algebras $R$ whose structure map $\mathcal O\to R$ is local and induces an isomorphism of residue fields; the residue field of $R$ is identified with $k$. Let $\Gamma$ be a topological group and let $\eta:\Gamma\to\{\pm1\}$ and $\Psi:\Gamma\to\mathcal O^\times$ be homomorphisms. A *lift* of $(\eta,\Psi)$ over $R\in\mathcal C_{\mathcal O}$ is a homomorphism $r:\Gamma\to\mathcal G_3(R)$ with the following two properties.

1. For all $a,b\in\{1,2,3\}$ and every integer $n\ge0$, the map $\gamma\mapsto\dot r(\gamma)_{ab}\bmod\mathfrak m_R^n$ from $\Gamma$ to $R/\mathfrak m_R^n$ is locally constant.
2. The composite of $r$ with $\mathcal G_3(R)\to\mathcal G_3(k)$ is $r_{\eta,\overline\Psi}$, where $\overline\Psi=\Psi\bmod\mathfrak m_{\mathcal O}$.

A lift has sign $\eta$. If $r$ is a lift over $R$ and $f:R\to R'$ is a homomorphism of $\mathcal O$-algebras in $\mathcal C_{\mathcal O}$, then $f\circ r$ is a lift over $R'$.

A *condition on lifts* is a property $P$ of pairs $(R,r)$, where $R\in\mathcal C_{\mathcal O}$ and $r$ is a lift over $R$. A *universal lift with condition $P$* is a pair $(R_P,r_P)$ of this kind such that, for every $R'\in\mathcal C_{\mathcal O}$: the pair $(R',f\circ r_P)$ has property $P$ for every homomorphism of $\mathcal O$-algebras $f:R_P\to R'$; and every lift $r'$ over $R'$ with property $P$ is $f\circ r_P$ for exactly one such $f$. A *universal lift* of $(\eta,\Psi)$ is a universal lift with the condition that every pair satisfies.

**The arithmetic data and the datum.** Fix an algebraic closure $\overline{\mathbb Q}$ of $\mathbb Q$ and, for a field $F\subset\overline{\mathbb Q}$, write $G_F=\operatorname{Gal}(\overline{\mathbb Q}/F)$. Let $K$, $\ell$, $\mathcal O\subset\overline{\mathbb Q}_\ell$, $N$, $e$ and $\psi$ be as in the theorem ([Selmer lengths and trace congruences](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy/)) and satisfy its conditions 1–4: $K\subset\overline{\mathbb Q}$ is an imaginary quadratic field, $\ell$ is a prime, $\mathcal O$ is a discrete valuation ring that is finite over $\mathbb Z_\ell$, and $\psi$ is a Dirichlet character modulo $N$ with values in $\mathcal O$. As on that page, $\psi$ and its component $\psi_\ell$ are regarded as characters of $G_{\mathbb Q}$, and $\Psi=\epsilon_\ell^e\psi:G_{\mathbb Q}\to\mathcal O^\times$. Write $G_{\mathbb Q_\ell}=\operatorname{Gal}(\overline{\mathbb Q}_\ell/\mathbb Q_\ell)$, let $I_\ell\subset G_{\mathbb Q_\ell}$ be its inertia subgroup, and write $\epsilon_\ell$ also for the $\ell$-adic cyclotomic character of $G_{\mathbb Q_\ell}$.

A *datum* $\mathfrak D$ for $(K,\ell,\mathcal O,N,e,\psi)$ consists of

- the homomorphism $\eta:G_{\mathbb Q}\to\{\pm1\}$ with kernel $G_K$;
- an element $c\in G_{\mathbb Q}$ that is a complex conjugation: there is an embedding $\varphi:\overline{\mathbb Q}\to\mathbb C$ with $\varphi(c(x))=\overline{\varphi(x)}$ for all $x$;
- an embedding of fields $j:\overline{\mathbb Q}\to\overline{\mathbb Q}_\ell$ and a continuous homomorphism $\lambda:G_{\mathbb Q_\ell}\to G_{\mathbb Q}$ with $s(j(x))=j(\lambda(s)(x))$ for all $s\in G_{\mathbb Q_\ell}$ and $x\in\overline{\mathbb Q}$;
- a subfield $K_v\subset\overline{\mathbb Q}_\ell$ of finite degree over $\mathbb Q_\ell$ such that, for $s\in G_{\mathbb Q_\ell}$, $\eta(\lambda(s))=1$ if and only if $s$ fixes $K_v$;

with the following four properties.

1. $\eta(\lambda(s))=1$ for every $s\in I_\ell$.
2. The kernel of $\psi_\ell\circ\lambda$ is open in $G_{\mathbb Q_\ell}$.
3. For all integers $m$ and $n\ge0$, the map $g\mapsto\Psi(g)^m\bmod\mathfrak m_{\mathcal O}^n$ is locally constant on $G_{\mathbb Q}$.
4. $\Psi(\lambda(s))=\epsilon_\ell(s)^e\,\psi_\ell(\lambda(s))$ for every $s\in I_\ell$.

Write $\eta_\ell=\eta\circ\lambda$, $\Psi_\ell=\Psi\circ\lambda$ and $\tau=\psi_\ell\circ\lambda$; these are homomorphisms on $G_{\mathbb Q_\ell}$.

**The local universal lift and its ideal.** Let $\mathfrak D$ be a datum and let $(R^{\rm loc},r^{\rm loc})$ be a universal lift of $(\eta_\ell,\Psi_\ell)$ on $G_{\mathbb Q_\ell}$. We define an ideal $I^{\rm loc}$ of $R^{\rm loc}$. Put $H=\ker\eta_\ell\cap\ker\tau$ and $I_H=H\cap I_\ell$. Put $\psi_1=\Psi_\ell$, $\psi_2=1$ and $\psi_3=\Psi_\ell^{-1}$, and read the indices of $\psi_a$, $c_a$, $N_a$, $t_a$ and $d_a$ below modulo $3$. Choose, once for $\mathfrak D$,

- an element $s_0\in I_H$ such that $\epsilon_\ell(s_0)$ has infinite order, and
- an element $\phi\in H$ such that the subgroup generated by $I_H$ and $\phi$ is dense in $H$ and such that $\phi\in\phi_0^mI_\ell$ for an integer $m\ge1$ and an element $\phi_0\in G_{\mathbb Q_\ell}$ with $|\phi_0(x)-x^\ell|_\ell<1$ for all $x\in\overline{\mathbb Q}_\ell$ with $|x|_\ell\le1$.

For $s\in G_{\mathbb Q_\ell}$ and $a\in\{1,2,3\}$ put $N_a(s)=\dot r^{\rm loc}(s)-\psi_a(s)\cdot1\in M_3(R^{\rm loc})$, and put $$c_a=\bigl(\psi_a(s_0)-\psi_{a+1}(s_0)\bigr)\bigl(\psi_a(s_0)-\psi_{a+2}(s_0)\bigr)\in\mathcal O.$$ Let $\mathfrak a\subset R^{\rm loc}$ be the ideal generated by the coefficients of the polynomials $$\det\bigl(X-\dot r^{\rm loc}(s)\bigr)-\prod_{a=1}^3\bigl(X-\psi_a(s)\bigr)\qquad(s\in I_H)$$ and by the entries of the matrices $N_1(s_1)N_2(s_2)N_3(s_3)$ for $s_1,s_2,s_3\in I_H$. Put $$t_a=\operatorname{tr}\bigl(N_{a+1}(s_0)\,N_{a+2}(s_0)\,\dot r^{\rm loc}(\phi)\bigr),\qquad d_a=c_{a+1}t_a-\epsilon_\ell(\phi)\,c_a\,t_{a+1},\qquad\delta=\ell\,d_1d_2,$$ and let $\mathfrak b$ be the ideal of the $x\in R^{\rm loc}$ with $\delta^nx\in\mathfrak a$ for some $n\ge0$. Then $I^{\rm loc}$ is the intersection of those prime ideals $P$ of $R^{\rm loc}$ that are minimal among the prime ideals containing $\mathfrak b$ and are contained in the kernel of every homomorphism of $\mathcal O$-algebras $x:R^{\rm loc}\to\mathcal O$ with $x\circ r^{\rm loc}=r_{\eta_\ell,\Psi_\ell}$. If there is no such $P$, then $I^{\rm loc}=R^{\rm loc}$.

**The deformation rings.** Let $g_1\in G_{\mathbb Q}$. Consider the following condition $P(g_1)$ on a lift $r$ of $(\eta,\Psi)$ on $G_{\mathbb Q}$ over $R\in\mathcal C_{\mathcal O}$.

1. $\dot r(c)=1$, and the entries in positions $(1,2)$ and $(2,1)$ of the matrix $\dot r(g_1)-\dot r(c\,g_1^{-1}c)$ are $0$.
2. $r(g)=1$ for every $g\in G_{\mathbb Q}$ that satisfies $r_{\eta,\overline\Psi}(g)=1$ and lies in the inertia group of a valuation subring of $\overline{\mathbb Q}$ whose maximal ideal does not contain $\ell$.
3. There is a homomorphism of $\mathcal O$-algebras $f:R^{\rm loc}\to R$ with $f(I^{\rm loc})=0$ and $r\circ\lambda=f\circ r^{\rm loc}$.

A *deformation ring of $\mathfrak D$ at $g_1$*, formed with $(R^{\rm loc},r^{\rm loc})$, is a universal lift $(S,r_S)$ of $(\eta,\Psi)$ on $G_{\mathbb Q}$ with condition $P(g_1)$.

The pair $(c,g_1)$ is *marked* if $$c^2=1,\qquad\eta(c)=-1,\qquad\Psi(c)=1,\qquad\eta(g_1)=1,\qquad\Psi(g_1)^2-1\in\mathcal O^\times.$$

**Points.** Let $(S,r_S)$ be a deformation ring of $\mathfrak D$ at $g_1$. A *local point* of $S$ is a homomorphism of $\mathcal O$-algebras $f:S\to\overline{\mathbb Q}_\ell$ with $|f(x)|_\ell<1$ for every $x$ in the maximal ideal of $S$. It gives the homomorphism $r_f=f\circ r_S:G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$, which has sign $\eta$, and the representation $$\rho_f=\dot r_f|_{G_K}:G_K\to\mathrm{GL}_3(\overline{\mathbb Q}_\ell).$$ Let $E_S\subset S$ be the $\mathcal O$-subalgebra generated by the entries $\dot r_S(g)_{ab}$, for $g\in G_{\mathbb Q}$ and $a,b\in\{1,2,3\}$, and let $S_0\subset E_S$ be the $\mathcal O$-subalgebra generated by the products of such entries in which the weights of the factors have sum $0$. For a homomorphism of $\mathcal O$-algebras $\xi:E_S\to\overline{\mathbb Q}_\ell$, a homomorphism $r:G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ is *obtained from $r_S$ by $\xi$* if $r$ has sign $\eta$ and $\dot r(g)_{ab}=\xi(\dot r_S(g)_{ab})$ for all $g$, $a$, $b$. For a local point $f$, the homomorphism $r_f$ is obtained from $r_S$ by $f|_{E_S}$.

**Conditions (I) and (II).** Let $r:G_{\mathbb Q}\to\mathcal G_3(\overline{\mathbb Q}_\ell)$ be a homomorphism with sign $\eta$, so that $\dot r|_{G_K}$ is a representation of $G_K$.

- (I) The only subspaces of $\overline{\mathbb Q}_\ell^3$ that all $\dot r(g)$, $g\in G_K$, map to themselves are $0$ and $\overline{\mathbb Q}_\ell^3$.
- (II) For every $g\in G_K$ the entries of $\dot r(g)$ of odd weight are $0$, and the only subspaces of $\overline{\mathbb Q}_\ell^2$ that all the matrices $$\dot r(g)^{\square}=\begin{pmatrix}\dot r(g)_{11}&\dot r(g)_{13}\\ \dot r(g)_{31}&\dot r(g)_{33}\end{pmatrix}\qquad(g\in G_K)$$ map to themselves are $0$ and $\overline{\mathbb Q}_\ell^2$.

A homomorphism $W:G_{\mathbb Q}\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)$ *extends the corner of $r$* if $W(g)=\dot r(g)^{\square}$ for every $g\in G_K$ and $\operatorname{tr}W(c)=0$.
