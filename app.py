from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")


gatsby_quotes = [
    {
        "id": 0,
        "quote": '''"His parents were shiftless and unsuccessful farm people — his imagination had never really accepted them as his parents at all. The truth was that Jay Gatsby, of West Egg, Long Island, sprang from his Platonic conception of himself. He was a son of God"(Fitzgerald 105).''',
        "analysis": (
            "This quote reveals the radical extent of Gatsby’s transformation of identity. Rather than accept his humble upbringings, "
            "Gatsby views his parents as 'shiftless and unsuccessful', seeing their lives as antithetical to his ambitions of attaining his idealized version of success: wealth and status. "
            "This incompatibility between Gatsby’s roots and his pursuit of the American Dream is why Gatsby feels the need to overcompensate for his old self through a new identity. "
            "The inauthenticity of this identity is emphasized through the phrases 'invented' and 'Platonic conception,' which highlight its detachment from reality. "
            "Furthermore, the description of Gatsby as a 'son of God' suggests that he sees himself as possessing the power to rewrite the past and will his imagined identity into reality, a recurring theme throughout the novel."
        ),
    },
    {
        "id": 1,
        "quote": '''“‘Can’t repeat the past?’ he cried incredulously. ‘Why of course you can!’”(Fitzgerald 118).''',
        "analysis": (
            "Here, again we see the theme of rewriting the past, as Gatsby believes his transformed identity will allow him to erase Daisy's feelings for Tom and recreate their past relationship. "
            "Fitzgerald uses Gatsby’s confidence to illustrate how the pursuit of the American Dream encourages the belief that self-determination and thus self-transformation can overcome all obstacles. "
            "However, the radical self-transformation Gatsby undergoes, and his denial of the finality of the past, foreshadows the collapse of his dreams as he is unable to recognize the limits of reinvention."
        ),
    },
    {
        "id": 2,
        "quote": '''"But with every word she was drawing further and further into herself, so he gave that up and only the dead dream fought on as the afternoon slipped away, trying to touch what was no longer tangible, struggling unhappily, undespairingly, toward that lost voice across the room"(Fitzgerald, 144).''',
        "analysis": (
            "This quote marks the moment Gatsby’s dreams begin to unravel as his carefully constructed identity begins to crumble. The description of the dream as 'no longer tangible' indicates its elusive nature, as it was built on an expectation that he could rewrite the past through an identity built on falsehoods. "
            "As Gatsby is unwilling to admit, Daisy has changed during her time with Tom, and the idealized future he has imagined is already unattainable. "
            "Through the realization of the death of Gatsby’s dream, Fitzgerald suggests that attaining success or the 'American Dream' proves elusive when the definition of that success is built off an inauthentic identity."
        ),
    },
]


@app.route("/gatsby")
def gatsby():
    return render_template("gatsby/index.html", quotes=gatsby_quotes)


@app.route("/gatsby/quote/<int:qid>")
def gatsby_quote(qid):
    q = gatsby_quotes[qid]
    return render_template(
        "gatsby/quote.html",
        quote=q,
        back_url="/gatsby",
        next_url=f"/gatsby/quote/{qid+1}" if qid + 1 < len(gatsby_quotes) else None,
    )


@app.route("/gatsby/summary")
def gatsby_summary():
    from flask import request
    qid = request.args.get('qid', None)
    bullets = None
    if qid is not None:
        try:
            qid_i = int(qid)
            q = gatsby_quotes[qid_i]
            bullets = [s.strip() for s in q['analysis'].split('. ') if s.strip()][:6]
        except Exception:
            bullets = None
    return render_template("gatsby/summary.html", bullets=bullets)



@app.route("/immigrant")
def immigrant():
    return render_template("immigrant/index.html", quotes=immigrant_quotes)



@app.route("/immigrant/assimilation")
def assimilation():
    
    return redirect(url_for("immigrant"))


@app.route("/immigrant/assimilation/quote/<int:qid>")
def assimilation_quote(qid):
    
    return redirect(url_for("immigrant_quote", qid=qid))



immigrant_quotes = [
    {
        "id": 0,
        "quote": '''“I am a Westernized critic, as Yang is Westernized writer, both of us subject to Western standards while also being subject to the standards of our original communities…the only solution offered from within a world that privileges authorship and the auteur, the accomplishment of the individual in a capitalist society, is to achieve the perfect grade, the A. If one stays within this world, how does one achieve this? What are the standards?”(Nguyen, “On True War Stories” 246).''',
        "analysis": '''Here, Ngyuen warns of the dangers of complete assimilation. At the beginning of the passage, he acknowledges that immigrants in the US are often caught between two worlds, “subject Western standards” as well the standards of their original community. However the proposed solution, achieving “the A” reflects only the values of the more dominant Western culture. By presenting the epitome of success through the lens of only Western values, Nguyen highlights how the pursuit of this “perfect grade” involves the rejection of one’s original identity. Additionally, Nguyen emphasizes the elusive nature of “the A” by questioning how one would achieve it, as the standards to such a seemingly objective sense of success are determined by external subjective judgement biased by one set of values. The pursuit of “the perfect grade” is analogous to the pursuit of the American Dream in the Great Gatsby, as both involve radical reinvention of one’s identity in order to achieve an idealized and unattainable version of success. ''',
    },
    {
        "id": 1,
        "quote": '''“I came to understand that in the United States, land of the fabled American dream, it is un-American to be a refugee. The refugee embodies fear, failure, and flight. Americans of all kinds believe that it is impossible for an American to become a refugee, although it is possible for refugees to become Americans and in that way be elevated one step closer to heaven”(Nguyen, “On Being a Refugee, an American—and a Human Being” 2).''',
        "analysis": '''Nguyen argues here that the American dream often encourages radical identity transformation as it frames the refugee identity as being incompatible with achieving success.  By characterizing the refugee as embodying “fear, failure, and flight,” Nyugen highlights how refugees are often defined by their displacement rather than resilience. In contrast, the American identity is portrayed as superior to the identity of the refugee, through the metaphor of being “elevated one step closer to heaven”. As a result of this hierarchical thinking, immigrants may feel pressured to suppress the refugee part of their identity, since “it is impossible for an American to become a refugee”. In this way, the American dream encourages conformity to narrowly defined “American identity” in order to align with society’s definition of success.''',
    },
    {
        "id": 2,
        "quote": '''“I am a refugee, an American, and a human being, which is important to proclaim, as there are many who think these identities cannot be reconciled”(Nguyen, “On Being a Refugee, an American—and a Human Being” 1).''',
        "analysis": '''Here, Nguyen makes the argument for integration instead of complete assimilation, challenging the notion that he must give up his identity as a refugee in order to be American. By declaring, “I am a refugee, an American, and a human being” he presents these identities as complimentary rather than contradictory and places equal value on each identity, unlike in the previous passage which elevated the American identity above all else. Furthermore, Nguyen highlights the social pressure immigrants face to choose between their identities by explaining how “there are many who think these identities cannot be reconciled”. By embracing all of his identities simultaneously, Nguyen suggests that success in America does not depend on picking one identity.''',
    },
]

@app.route("/immigrant/integration")
def integration():
    
    return redirect(url_for("immigrant"))


@app.route("/immigrant/quote/<int:qid>")
def immigrant_quote(qid):
    q = immigrant_quotes[qid]
    return render_template(
        "immigrant/quote.html",
        quote=q,
        back_url="/immigrant",
        next_url=f"/immigrant/quote/{qid+1}" if qid + 1 < len(immigrant_quotes) else None,
    )




@app.route("/immigrant/integration/quote/<int:qid>")
def integration_quote(qid):
    
    return redirect(url_for("immigrant_quote", qid=qid))





@app.route("/stats")
def stats():
    from flask import request
    
    return render_template("stats/index.html")


@app.route("/stats/economic")
def stats_economic():
    study = {
        "title": "Economic Study",
        "analysis": "",
    }
    return render_template("stats/economic.html", title=study['title'], analysis=study['analysis'])


@app.route("/stats/psychological")
def stats_psychological():
    study = {
        "title": "Psychological Study",
        "analysis": "",
    }
    return render_template("stats/psychological.html", title=study['title'], analysis=study['analysis'])

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)
