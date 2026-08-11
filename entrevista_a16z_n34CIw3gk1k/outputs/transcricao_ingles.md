# Transcrição integral em inglês

- Fonte utilizada: https://x.com/a16z/status/2086845184785203468
- Modelo: `openai/whisper-large-v3-turbo` via `faster-whisper`
- Regra editorial: transcrição integral; sem resumo e sem preenchimento de lacunas.

## 00:00:00–00:05:00

[00:00:00–00:00:04] **Alejandro:** I'm investing more today in tokens than in knowledge workers.

[00:00:04–00:00:06] **Alejandro:** We could build superhuman agents.

[00:00:07–00:00:09] **Alejandro:** This means that by every dimension that matters,

[00:00:09–00:00:13] **Alejandro:** our agents would outperform the best human we had ever hired.

[00:00:13–00:00:16] **Host:** The most ambitious companies listening to this will decide to follow suit,

[00:00:16–00:00:20] **Host:** which is you decided to build an agent per customer.

[00:00:21–00:00:26] **Alejandro:** Every day, between 100 and 200,000 agents get instantiated

[00:00:26–00:00:29] **Alejandro:** specifically for this customer with its own virtual machine.

[00:00:29–00:00:33] **Host:** There's a lot of people worried about how the organizations of the future are going to look like

[00:00:33–00:00:36] **Host:** and the role that humans are going to play.

[00:00:36–00:00:40] **Alejandro:** If you haven't faced fear before, you haven't felt it, then you haven't tried AI.

[00:00:40–00:00:44] **Alejandro:** We launched a program inside Kavak that's called the Jedi Academy.

[00:00:44–00:00:49] **Alejandro:** From the CEO to like AI engineers to mechanics, we train everyone.

[00:00:49–00:00:53] **Alejandro:** And after six weeks, they launch state-of-the-art agents to production.

[00:00:53–00:00:57] **Host:** What advice do you have to future founders or first-time founders that might be listening?

[00:00:57–00:00:59] **Alejandro:** What works right now is...

[00:00:59–00:01:04] **Host:** Welcome back to the a16z podcast.

[00:01:05–00:01:07] **Host:** Today, we have Ale Maza, the head of AI at Kavak.

[00:01:07–00:01:11] **Host:** We're going to discuss today the transformation that Ale led within Kavak

[00:01:11–00:01:13] **Host:** to turn into an AI-native company.

[00:01:13–00:01:15] **Host:** Thank you, Ale, for being with us today.

[00:01:15–00:01:16] **Alejandro:** Thanks for having me.

[00:01:16–00:01:20] **Host:** Before starting at Kavak, you were running a company called Opi Analytics.

[00:01:21–00:01:21] **Alejandro:** That's right.

[00:01:22–00:01:26] **Host:** And you were very much into AI before ChatGPT.

[00:01:26–00:01:28] **Host:** You want to tell us a little bit about that journey?

[00:01:28–00:01:29] **Alejandro:** Yes, yes, of course.

[00:01:29–00:01:31] **Alejandro:** Well, we called it machine learning back then.

[00:01:31–00:01:33] **Alejandro:** It was a different family of algorithms.

[00:01:33–00:01:41] **Alejandro:** And we founded a company with this very ambitious vision there that new machine learning models

[00:01:41–00:01:45] **Alejandro:** would be so powerful that they could solve any complex problem.

[00:01:46–00:01:47] **Alejandro:** This was pre-Transformers, right?

[00:01:47–00:01:49] **Alejandro:** This was like 2013.

[00:01:50–00:01:51] **Alejandro:** So we started building the company that way.

[00:01:51–00:01:57] **Alejandro:** And I think we were like 10 years ahead of time, but we built a great company.

[00:01:57–00:02:05] **Alejandro:** We served like 1,400, 500 companies around like risk algorithms, logistics, forecasting, marketing.

[00:02:05–00:02:18] **Alejandro:** But really the power of what Transformers and then the ChatGPT moment when it arrived make things very clearly

[00:02:18–00:02:29] **Alejandro:** that we could now build a whole new company and way of building companies.

[00:02:29–00:02:33] **Alejandro:** And we joined Kavak and Carlos to build it.

[00:02:33–00:02:34] **Host:** Amazing.

[00:02:34–00:02:34] **Host:** All right.

[00:02:34–00:02:39] **Host:** So we're going to spend the bulk of this podcast talking about exactly how you've identified Kavak.

[00:02:39–00:02:43] **Host:** But maybe just to start, what does Kavak do and what is your role there?

[00:02:43–00:02:47] **Alejandro:** Kavak started out as a used car marketplace.

[00:02:47–00:02:53] **Alejandro:** So we buy cars, we refurbish them, and then we sell them and finance them.

[00:02:53–00:03:02] **Alejandro:** But to do that, we also had to build a fintech and a logistics company and the Carfax and like

[00:03:02–00:03:06] **Alejandro:** basically all the infrastructure for this to work didn't exist in LATAM.

[00:03:06–00:03:10] **Alejandro:** So we had to build everything vertically so we could serve our customers the right way.

[00:03:11–00:03:14] **Host:** I'm going to sort of start with the framing of what the architecture looks like.

[00:03:14–00:03:17] **Host:** So a consumer comes in and says, I want to sell my car.

[00:03:17–00:03:19] **Host:** Like, how many agents do they touch?

[00:03:19–00:03:20] **Host:** Like, what's the harness look like?

[00:03:20–00:03:22] **Host:** Like, ground us in how you design this.

[00:03:22–00:03:22] **Alejandro:** Right.

[00:03:22–00:03:27] **Alejandro:** So we bet the company in transforming to a company run by agents.

[00:03:27–00:03:37] **Alejandro:** The questions we ask ourselves is, how would we build Kavak in 2035 with Fable 10 or GPT-10 level intelligence?

[00:03:37–00:03:43] **Alejandro:** And actually, that company looks very different than what we had built or what we had back then.

[00:03:44–00:03:52] **Alejandro:** So when a customer comes in right now, agent will get spawned specifically for this customer with its own virtual machine.

[00:03:52–00:04:01] **Alejandro:** It will remember years of interaction of these customers with Kavak, what they visited in the webpage or a call they had two years ago.

[00:04:01–00:04:14] **Alejandro:** So remember everything like in its memory, come up with a strategy and set a long-term goal to maximize the lifetime value of this customer and do whatever it takes to make the customer happy.

[00:04:14–00:04:20] **Alejandro:** And convert them into, like, all our different products, like, across time.

[00:04:21–00:04:31] **Alejandro:** And this is a completely new and groundbreaking architecture at scale, I think, because, like, people are still building multi-agent system with experts.

[00:04:31–00:04:44] **Alejandro:** And we realized to bet that long-running agents with hard goals, not just workflows, could maximize our customers' satisfaction and, obviously, their lifetime value.

[00:04:44–00:04:45] **Host:** Awesome.

[00:04:45–00:04:45] **Host:** Okay.

[00:04:45–00:04:47] **Host:** So we're going to jump to the nuances of that.

[00:04:47–00:04:53] **Host:** But maybe versus many companies that say, hey, we want to be agentic, and they try some workflows.

[00:04:53–00:04:58] **Host:** You guys took the just rip, like, we had to make this work.

[00:04:58–00:04:59] **Host:** You had to downsize dramatically.

## 00:05:00–00:10:00

[00:05:00–00:05:02] **Host:** It didn't work for a year.

[00:05:02–00:05:02] **Host:** Right.

[00:05:03–00:05:07] **Host:** So do you want to talk through, obviously, you had to tune a lot of things to make that work.

[00:05:07–00:05:12] **Host:** Like, describe the harness at that time and, like, what models you were using and sort of specifically.

[00:05:12–00:05:16] **Alejandro:** So there were, like, three main decisions that we had to make.

[00:05:17–00:05:23] **Alejandro:** The first, and this is where I think many companies are stuck right now, is the first instinct is, okay,

[00:05:23–00:05:24] **Alejandro:** let's adopt AI.

[00:05:25–00:05:31] **Alejandro:** And you basically leave your structure as it is and just give ChatGPT or Claude to your team.

[00:05:31–00:05:33] **Alejandro:** And then there's no efficiencies.

[00:05:33–00:05:36] **Alejandro:** Your customers have the same problems and nothing happens, right?

[00:05:36–00:05:43] **Alejandro:** And so you need to redesign your whole company around the agents and around the future capabilities.

[00:05:43–00:05:52] **Alejandro:** And this means really, like, rebuilding most of your APIs, rebuilding your system so the agents can use them to perform.

[00:05:52–00:05:57] **Alejandro:** Then you need to start generating the data and the feedback loops to fine-tune these agents.

[00:05:57–00:06:01] **Alejandro:** The only way to really make them work is if you teach them.

[00:06:01–00:06:02] **Alejandro:** Like, how do you teach them?

[00:06:02–00:06:04] **Alejandro:** You put them out in the open.

[00:06:04–00:06:05] **Alejandro:** You put them in front of customers.

[00:06:06–00:06:06] **Alejandro:** You get that data.

[00:06:06–00:06:07] **Alejandro:** You get those evals.

[00:06:07–00:06:11] **Alejandro:** And then you train your agents.

[00:06:12–00:06:17] **Alejandro:** And this is the second bet that we made, that we could build superhuman agents.

[00:06:17–00:06:24] **Alejandro:** This means that by every dimension that matters, like conversion, lifetime value, customer experience,

[00:06:24–00:06:29] **Alejandro:** our agents would outperform the best human we had ever hired.

[00:06:29–00:06:30] **Alejandro:** And we put them in front of the hardest problems.

[00:06:30–00:06:37] **Alejandro:** And finally, you start to change how you measure the success of the company.

[00:06:37–00:06:39] **Alejandro:** Kavak was a transactional company.

[00:06:40–00:06:46] **Alejandro:** We used to measure how many cars we bought, how many cars we sold, how many brakes we needed to, brake pads we needed to buy.

[00:06:46–00:06:59] **Alejandro:** And we moved to a relational company where now I have 10 million customers in my database and I have agents assigned to most of them with the task of maximizing their lifetime value.

[00:06:59–00:07:05] **Alejandro:** Now, we're selling cars and personal loans and very high-ticket items.

[00:07:05–00:07:15] **Alejandro:** So just activating 1% of this customer base, it's like hundreds of millions of dollars if we do it the right way.

[00:07:15–00:07:21] **Alejandro:** So it's a bet that made sense for us because of our industry, because of the ticket, and because at the end of the day,

[00:07:22–00:07:27] **Alejandro:** customers need to build trust with a company because they're buying a used car.

[00:07:27–00:07:34] **Alejandro:** And the way to build trust is to know them and to plan and nurture a long-term relationship.

[00:07:35–00:07:37] **Host:** Ale, I just wanted to double-click on something.

[00:07:37–00:07:39] **Host:** You know, evals over agent demos.

[00:07:40–00:07:40] **Host:** Yeah.

[00:07:40–00:07:47] **Host:** You probably get pitched a lot of agents and, you know, it's never been easier to build things like before.

[00:07:47–00:07:51] **Host:** But one of the questions is, like, how do you guys go about evaluating this?

[00:07:51–00:07:56] **Host:** Because not everybody tests them across 90% of the customer interactions to see if they're really working.

[00:07:56–00:08:04] **Host:** And, you know, you guys, I believe, is about 98% of the interactions or something like that are now handled by agents.

[00:08:04–00:08:04] **Alejandro:** Yes, totally.

[00:08:05–00:08:13] **Alejandro:** So to give you a sense of the scale, like 96% of all interactions are handled by agents.

[00:08:14–00:08:16] **Alejandro:** So no humans there.

[00:08:17–00:08:21] **Alejandro:** Like 95% of all transactions are completely handled by agents.

[00:08:21–00:08:25] **Alejandro:** Obviously, you meet a human when you pick up your car, like there's someone physically there to give you the keys.

[00:08:25–00:08:31] **Alejandro:** But the rest of the experience of the journey is handled by an agent.

[00:08:31–00:08:38] **Alejandro:** Every day, between 100,000 and 200,000 agents get instantiated in a day.

[00:08:38–00:08:39] **Alejandro:** They wake up.

[00:08:39–00:08:44] **Alejandro:** They work sometimes for three minutes, sometimes for eight hours, sometimes for three days.

[00:08:44–00:08:49] **Alejandro:** And they, like, set an alarm clock for their next task and go back to sleep.

[00:08:49–00:08:52] **Alejandro:** So the scale of this is just amazing.

[00:08:53–00:08:53] **Alejandro:** And it's working.

[00:08:53–00:08:57] **Alejandro:** Like, now, how do you get this to work at scale?

[00:08:58–00:09:01] **Alejandro:** And the answer you mentioned is evals.

[00:09:01–00:09:04] **Alejandro:** Like, I like to move extremely fast.

[00:09:05–00:09:08] **Alejandro:** But in order to move fast, you need to have brakes, right?

[00:09:08–00:09:08] **Alejandro:** Imagine a car.

[00:09:10–00:09:13] **Alejandro:** You'll hit on the gas just if you have the right brakes.

[00:09:14–00:09:15] **Alejandro:** And AI is super powerful.

[00:09:15–00:09:22] **Alejandro:** And I've seen many companies get this wrong because they try to go slow because they don't have the right brakes.

[00:09:22–00:09:24] **Alejandro:** So I thought about it the other way around.

[00:09:24–00:09:25] **Alejandro:** Like, how fast can we go?

[00:09:26–00:09:28] **Alejandro:** Well, it depends on the quality of our evals.

[00:09:28–00:09:43] **Alejandro:** So a good rule of thumb here is we spend about the same amount of time, engineer time, tokens, and money on building the evals than building the agents.

[00:09:43–00:09:48] **Alejandro:** And this is how you get better and better and better, not letting evals as an afterthought.

[00:09:48–00:09:49] **Alejandro:** So what do we measure?

[00:09:50–00:09:53] **Alejandro:** First and foremost, like, the results for the business.

[00:09:53–00:09:56] **Alejandro:** Like, if my customer is happy, they'll buy a car.

[00:09:56–00:09:59] **Alejandro:** They'll get their loan approved.

[00:09:59–00:10:01] **Alejandro:** They'll sell a car to us.

## 00:10:00–00:15:00

[00:10:01–00:10:03] **Alejandro:** And that's the, like, first check.

[00:10:03–00:10:05] **Alejandro:** Like, did it convert?

[00:10:05–00:10:07] **Alejandro:** And that's where most things break.

[00:10:07–00:10:20] **Alejandro:** Like, I see companies, like, measuring number of calls or minutes during the call or some, like, superficial KPIs that give you some information, but that doesn't really work.

[00:10:20–00:10:30] **Alejandro:** Like, the important thing is did this customer convert, is it bringing value to the customer, and is the customer happy to re-engage with us after a while?

[00:10:30–00:10:41] **Alejandro:** And once you get those evals connected, then it's just optimizing the right agentic architecture and giving the agent skills to scale this and cater to millions of customers.

[00:10:43–00:10:43] **Host:** It's really, really amazing.

[00:10:43–00:11:02] **Host:** And, you know, related to this is, like, okay, so you create the right evals, you know, it's working, you know, some people, some companies still feel a little bit risk-averse and putting them in front of the customers and being able to perform the highest leverage tasks, which in your case would be selling.

[00:11:02–00:11:04] **Host:** Do your agents really sell to customers?

[00:11:04–00:11:05] **Alejandro:** Yes.

[00:11:05–00:11:08] **Alejandro:** So we never built customer support or customer service agents.

[00:11:09–00:11:11] **Alejandro:** We built, like, sales agents.

[00:11:11–00:11:15] **Alejandro:** It's extremely hard to sell a car in Latin America.

[00:11:16–00:11:18] **Alejandro:** So imagine someone wanting to buy a car.

[00:11:19–00:11:22] **Alejandro:** They can choose, like, amongst, like, 20,000 SKUs.

[00:11:22–00:11:29] **Alejandro:** Then they need to pick, like, financing and go through the financing process, insurance and coverage.

[00:11:29–00:11:32] **Alejandro:** And then they're probably trading in their car.

[00:11:32–00:11:34] **Alejandro:** So we need to quote that car.

[00:11:34–00:11:48] **Alejandro:** So it's a process that if someone does it or the way Kavak did it back in 2020, 2021, was you need to be extremely good at 15 different things and have 15 different experts in 15 different teams.

[00:11:48–00:12:00] **Alejandro:** And usually the person would go and speak with the expert in financing, the expert in car advisory, the expert in buying, the expert in insurance, and they'll build a package and buy a car.

[00:12:00–00:12:03] **Alejandro:** And that's extremely hard to do.

[00:12:03–00:12:19] **Alejandro:** But, like, the first thing we did was, okay, can we get an agent to be better than the expert in each of these things and then put it together and have, like, a mega expert that's an expert in insurance, financing, et cetera.

[00:12:19–00:12:22] **Alejandro:** And that's who we put in front of the customer.

[00:12:22–00:12:24] **Alejandro:** So the experience for the customer is amazing.

[00:12:24–00:12:31] **Alejandro:** We tripled NPS and customer satisfaction score by putting the agent in front of the customer.

[00:12:32–00:12:37] **Alejandro:** And at first it converted, like, 50% more than our human team.

[00:12:37–00:12:43] **Alejandro:** And now it's converting over that, like, 2.1x more.

[00:12:44–00:12:45] **Alejandro:** So it's a completely different company.

[00:12:45–00:12:46] **Alejandro:** So your agents are better sellers.

[00:12:47–00:12:47] **Alejandro:** Totally better.

[00:12:47–00:12:59] **Alejandro:** And you get this, right, because they're experts, and they're infinitely patient, and they know all your history, and they can plan for the long term, and they never get tired.

[00:12:59–00:13:09] **Alejandro:** So, and if they make a mistake, they learn it, and the next day, not just them, but the other 200,000 agents will have learned from that mistake.

[00:13:09–00:13:16] **Alejandro:** So that's the feedback loop that we engaged, and that's showing in the growth and results and satisfaction of our customers.

[00:13:16–00:13:25] **Host:** One of the, well, two of the very cool things I think about Kavak is I think the world has gotten comfortable with AI can do customer service.

[00:13:25–00:13:26] **Host:** It's still very hard to do well.

[00:13:26–00:13:34] **Host:** But, you know, as Gabe said, there's still a view that, well, customers aren't going to want to buy expensive things from AI, and you are proving them wrong.

[00:13:34–00:13:35] **Alejandro:** Yes.

[00:13:35–00:13:42] **Host:** The next layer on that is, well, you're not actually going to be able to do regulated financial services end-to-end with AI.

[00:13:42–00:13:51] **Host:** But if you walk through what you're doing, you are underwriting a thin or no-file customer, pricing them correctly, doing servicing.

[00:13:51–00:14:04] **Host:** So maybe talk through how did you write the evals to get comfortable with that, and then versus, I don't know, going to a bank branch or even a fintech, sort of how is that experience that much better?

[00:14:04–00:14:18] **Alejandro:** So the first financial product that we launched was a car loan, and usually in Mexico and in some emerging markets, it'll get like two months or more to get a car loan approved.

[00:14:18–00:14:29] **Alejandro:** We usually approve it in under three minutes, which is like pretty cool, because we have all this data around the customer and the car.

[00:14:30–00:14:45] **Alejandro:** And if the customer can't pay for the car anymore, they'll just return it to us, and we can give them a cheaper car, and then they pay a smaller amount each month, and they like get out of the water, which is amazing about the vertical integration of the business.

[00:14:45–00:14:54] **Alejandro:** But then, like, when we started launching other financial products, we realized that this is a very important decision for the customer, right?

[00:14:54–00:15:08] **Alejandro:** Like, they usually take three to four months to make up their mind in buying a car and getting a loan or getting a personal loan, like a large personal loan that we also do.

## 00:15:00–00:20:00

[00:15:08–00:15:22] **Alejandro:** So if you get to know your customer throughout this process and make the process easy for them, then just your conversion and retention metrics start going through the roof.

[00:15:22–00:15:49] **Alejandro:** It's not just the transaction, it's understanding each customer personally and get them to convert when they're ready with a very deep personalization of the interest rate, the risk, the max amount of the loan in a way that makes sense for the portfolio as a whole, obviously, but that's optimized to the risk level and probably the other offers that the customer is getting.

[00:15:49–00:15:55] **Host:** And then maybe give us just to be, you know, evals are always a very hot topic, you kind of led with that.

[00:15:55–00:16:06] **Host:** What is an example of maybe a hard-to-design area for evals or one where you had to spend an extra amount of time with just given the fact that, like, there's real money PII at risk?

[00:16:06–00:16:06] **Host:** Right.

[00:16:06–00:16:06] **Alejandro:** Yeah.

[00:16:06–00:16:23] **Alejandro:** So when we decided to redesign the company around AI, you asked the question, okay, is AI going to be able to do this job, like even the CEO job or jobs where the leadership is?

[00:16:23–00:16:25] **Alejandro:** And the answer, honestly, is probably yes.

[00:16:25–00:16:28] **Alejandro:** Like in 2035 with a rate of improvement, it will be able to do.

[00:16:28–00:16:30] **Alejandro:** So we said, okay, let's try it now.

[00:16:31–00:16:34] **Alejandro:** Let's try and build an AI CEO.

[00:16:35–00:16:38] **Alejandro:** So we carved out a city in Mexico.

[00:16:38–00:16:39] **Alejandro:** It's Cuernavaca.

[00:16:39–00:16:44] **Alejandro:** And we put like an agent in one of our harnesses as a CEO.

[00:16:45–00:16:49] **Alejandro:** And it starts learning and it starts making decisions and evaluating on those decisions.

[00:16:50–00:16:53] **Alejandro:** And it's only been running for six weeks now.

[00:16:53–00:16:58] **Alejandro:** The goal of the first month was to double the profits of Cuernavaca.

[00:16:58–00:17:09] **Alejandro:** It didn't reach it, but it was 1.5x, like 50% more profits just by managing the city, which is crazy, right?

[00:17:09–00:17:10] **Alejandro:** It's amazing.

[00:17:10–00:17:12] **Alejandro:** And it's the CEO.

[00:17:12–00:17:16] **Alejandro:** Like people were like, that was the last job AI was supposed to take.

[00:17:16–00:17:18] **Alejandro:** And no, it isn't really.

[00:17:18–00:17:20] **Alejandro:** And how did this happen?

[00:17:20–00:17:40] **Alejandro:** And it's like a very smart person, like Fields Medal-level smart, like going into every single number, every single customer, making the perfect forecast and going to micromanage every single thing that needs to be executed every day to reach a plan.

[00:17:40–00:17:52] **Alejandro:** So he'll literally send messages to all the physical workers in Cuernavaca with their plans for the day and ask them to send voice notes back to know their progress.

[00:17:53–00:17:55] **Alejandro:** So customer satisfaction grew.

[00:17:56–00:17:57] **Alejandro:** We got a better inventory.

[00:17:58–00:18:03] **Alejandro:** We rotated better, better financing penetration, like every KPI started to improve.

[00:18:03–00:18:06] **Alejandro:** So it's super cool and super exciting.

[00:18:06–00:18:15] **Alejandro:** Now, what are the jobs where we think we're still like training and hiring humans?

[00:18:15–00:18:17] **Alejandro:** Those are related to the physical world.

[00:18:17–00:18:24] **Alejandro:** So when we talk about mechanics, Cuernavaca has around, I think in Mexico, around 800 mechanics.

[00:18:24–00:18:29] **Alejandro:** There's lots of dexterity and senses that's super hard to substitute.

[00:18:30–00:18:33] **Alejandro:** So there, we also build these agents with the exact same harness that's scaling.

[00:18:34–00:18:37] **Alejandro:** And the mechanics have the sidekick.

[00:18:37–00:18:48] **Alejandro:** I was telling you guys earlier, it's like the movie Ratatouille, like the mouse that's actually a chef collaborating with a human.

[00:18:48–00:18:49] **Alejandro:** It's kind of like that.

[00:18:49–00:18:50] **Alejandro:** So it's a sidekick.

[00:18:50–00:18:51] **Alejandro:** We call it El Mike.

[00:18:52–00:18:59] **Alejandro:** And it tells them how to inspect a car and gives them tips and shows them the way to do it.

[00:18:59–00:19:07] **Alejandro:** And the quality of inspections, again, went through the roof, we're inspecting faster, we're repairing faster, it's cheaper.

[00:19:07–00:19:11] **Alejandro:** But most importantly, we're delivering higher quality cars.

[00:19:13–00:19:19] **Alejandro:** Warranties came down around like 20, 26% since we launched.

[00:19:19–00:19:22] **Alejandro:** And customer satisfaction, again, went up.

[00:19:23–00:19:24] **Alejandro:** So it's about this.

[00:19:24–00:19:36] **Alejandro:** Like, how would you design your organization from scratch with abundant superintelligence that's cheap and just go build it?

[00:19:37–00:19:51] **Host:** Now, this is a good segue to a key topic right now in Silicon Valley where, you know, there's a lot of people worried about how the organizations of the future are going to look like and the role that humans are going to play.

[00:19:51–00:19:51] **Host:** Yes.

[00:19:51–00:19:53] **Host:** And I think you touched a little bit on that.

[00:19:53–00:19:57] **Host:** And so we'd love to hear, yeah, like how you guys are thinking about that.

[00:19:57–00:19:57] **Host:** Yes.

[00:19:58–00:20:00] **Host:** And the organizations.

## 00:20:00–00:25:00

[00:20:00–00:20:00] **Host:** Yeah.

[00:20:01–00:20:01] **Alejandro:** Totally.

[00:20:01–00:20:06] **Alejandro:** So we took that question very seriously three years ago.

[00:20:06–00:20:11] **Alejandro:** And the truth is that everyone's job will change.

[00:20:12–00:20:21] **Alejandro:** So, and what we were doing a couple of years ago will probably be performed better by an AI agent.

[00:20:22–00:20:22] **Alejandro:** Right?

[00:20:22–00:20:23] **Alejandro:** So what does this mean?

[00:20:23–00:20:25] **Alejandro:** Like, we need to train everyone.

[00:20:26–00:20:36] **Alejandro:** So, so we launched a program inside Kavak that's called the Jedi Academy where anyone from Kavak, like from the CEO to, yeah.

[00:20:36–00:20:36] **Alejandro:** And it's awesome.

[00:20:37–00:20:43] **Alejandro:** Like from the CEO to like AI engineers to mechanics, like going to the academy.

[00:20:43–00:20:49] **Alejandro:** It's super hard. Like, I've led it myself.

[00:20:49–00:20:50] **Host:** You designed the program.

[00:20:50–00:20:51] **Alejandro:** I designed the program.

[00:20:51–00:20:52] **Alejandro:** But constantly.

[00:20:52–00:20:53] **Host:** Constantly.

[00:20:53–00:20:57] **Alejandro:** Because you need to be upgrading the program because everything's changing so fast.

[00:20:57–00:21:04] **Alejandro:** And there's like, you can't send these people like outside to Stanford to, to learn this because like, it's new stuff.

[00:21:04–00:21:04] **Alejandro:** Right?

[00:21:05–00:21:07] **Alejandro:** So we train everyone.

[00:21:07–00:21:14] **Alejandro:** And after six weeks, they launch state-of-the-art agents, AI agents to production.

[00:21:14–00:21:21] **Alejandro:** And it's mechanics and finance guys and engineers, like everyone can do it.

[00:21:21–00:21:27] **Alejandro:** And what this generated is maybe this person won't become an AI engineer.

[00:21:27–00:21:32] **Alejandro:** Some of them have, but they, they know how to collaborate with this new technology.

[00:21:32–00:21:32] **Alejandro:** Right?

[00:21:32–00:21:36] **Alejandro:** So the way we looked about it was, guys, there, there's no way back.

[00:21:36–00:21:38] **Alejandro:** Like this is the way Kavak is going.

[00:21:38–00:21:40] **Alejandro:** This is the way the company will look like.

[00:21:40–00:21:46] **Alejandro:** These are the changes for the engineering team, the finance team, the product team.

[00:21:46–00:21:48] **Alejandro:** Like, this is what's going to change.

[00:21:49–00:21:56] **Alejandro:** You have the choice to like train and, and get the skills to perform in this new reality, in this new world.

[00:21:58–00:22:01] **Alejandro:** Or maybe leave Kavak if this is not for you, but this is the way we're going.

[00:22:02–00:22:03] **Alejandro:** And we're great.

[00:22:04–00:22:07] **Alejandro:** Like, like we, we, we strengthened the culture and we were super excited.

[00:22:08–00:22:12] **Alejandro:** And people really know how to build these agentic systems.

[00:22:12–00:22:19] **Alejandro:** And then if you look at Kavak now, any process, it's really a collaboration of agents and humans.

[00:22:19–00:22:23] **Alejandro:** And sometimes like agents are the bosses or, of, of humans.

[00:22:23–00:22:25] **Alejandro:** And sometimes humans are designing the agents.

[00:22:25–00:22:29] **Alejandro:** But I think we, we managed to really build this and change this.

[00:22:30–00:22:38] **Alejandro:** And, and it's through this idea that we need to be learning every day and things will continue to change.

[00:22:38–00:22:46] **Alejandro:** And the only way to, to continue being relevant is to upgrade your skills every month or every couple of months.

[00:22:46–00:22:50] **Host:** But you do have, or did have, you know, thousands of people.

[00:22:51–00:22:53] **Host:** Now agents do most things.

[00:22:53–00:22:53] **Host:** Yes.

[00:22:53–00:22:56] **Host:** So like, what is the org structure of Kavak?

[00:22:57–00:22:59] **Host:** Like, does the middle management concept even exist anymore?

[00:22:59–00:23:00] **Host:** Like, what does your org look like?

[00:23:00–00:23:00] **Alejandro:** Right.

[00:23:01–00:23:06] **Alejandro:** So the way it looks like now is very flat teams, very senior teams, super empowered.

[00:23:06–00:23:13] **Alejandro:** If you look at a team, you'll have engineering, AI, like operations, like everything.

[00:23:13–00:23:21] **Alejandro:** And they're either building the agents, working for the agents, or being in the physical world in front of the customer.

[00:23:22–00:23:24] **Alejandro:** Like most of our organization looks like that.

[00:23:24–00:23:36] **Alejandro:** So, so it's really built around, around the idea of how organizations will look like in the future and around AI and really harnessing this, this new technology.

[00:23:36–00:23:43] **Alejandro:** Obviously, this required lots of retraining because in 2023 or 2022, no one was building agents.

[00:23:43–00:23:47] **Alejandro:** No one was helping agents or taking orders from, from agents.

[00:23:47–00:23:56] **Alejandro:** And the way you cater to the physical world or the customers was in a different way than if an agent's telling you what to do or helping you make your job better.

[00:23:56–00:23:57] **Host:** Yep.

[00:23:57–00:24:01] **Alejandro:** And so it's a completely different structure than, than we had just two years ago.

[00:24:01–00:24:01] **Host:** Yeah.

[00:24:01–00:24:05] **Host:** Explain, we talked about this before, what working for the agents look like.

[00:24:05–00:24:07] **Host:** Like, I think the way you described it was an agentic system.

[00:24:08–00:24:11] **Host:** And then sometimes when it fails, it's like, oh, that's kicked out to kind of a human queue.

[00:24:11–00:24:11] **Host:** Right.

[00:24:11–00:24:12] **Host:** But then that's lost.

[00:24:13–00:24:14] **Host:** And so how have you brought that together?

[00:24:14–00:24:22] **Alejandro:** So like the, the, we see human in the loops and, and, and most of these agentic systems in production right now, like large scale agentic systems.

[00:24:22–00:24:33] **Alejandro:** Usually if an agent hits a wall or can't perform anymore, it'll like send the, this case or this customer to a tier two support and forget about it.

[00:24:34–00:24:37] **Alejandro:** That doesn't really work because you don't close the loops.

[00:24:37–00:24:41] **Alejandro:** So you don't generate the data to train the agent to do this better.

[00:24:41–00:24:46] **Alejandro:** What works right now is we have an agent that's obsessed with each of the customers, like millions of this.

[00:24:46–00:24:55] **Alejandro:** They have access to every single API, every single skill, like, and we have agents building those humans, building those skills for them.

[00:24:55–00:25:02] **Alejandro:** And then if an agent hits a wall or cancel something, it'll call this API saying, I need help.

## 00:25:00–00:30:00

[00:25:02–00:25:05] **Alejandro:** And on the other side, it's not an agent or software.

[00:25:06–00:25:08] **Alejandro:** It's a human helping them out.

[00:25:08–00:25:14] **Alejandro:** But if you map this out in an org chart, it's really human teams that have an agent.

[00:25:14–00:25:15] **Alejandro:** I'm getting better results.

[00:25:15–00:25:16] **Host:** It's super clear.

[00:25:16–00:25:18] **Host:** Like, it makes sense.

[00:25:18–00:25:19] **Host:** That's actually a perfect segue.

[00:25:19–00:25:24] **Host:** And I know you get lots of leaders at larger institutions inbounding to you.

[00:25:24–00:25:25] **Host:** So maybe this will save you many phone calls.

[00:25:25–00:25:31] **Host:** But I think rationally, many leaders of companies intuitively understand this.

[00:25:31–00:25:37] **Host:** It is very hard still to deploy AI through their organization.

[00:25:37–00:25:38] **Host:** Like, the models are good enough.

[00:25:38–00:25:39] **Host:** You know that.

[00:25:39–00:25:40] **Host:** It's an org problem.

[00:25:40–00:25:41] **Host:** It's a psychology problem.

[00:25:41–00:25:43] **Host:** Like, what advice do you have or what have you seen?

[00:25:43–00:25:45] **Alejandro:** I think it's two things.

[00:25:45–00:25:49] **Alejandro:** The first is it has to be top down because of this.

[00:25:50–00:26:04] **Alejandro:** Like, if you just get adoption, it won't go anywhere because it's hard to generate this taste or strategy for people to bottom up, decide what to build and whatnot, and come up with something that works for the company.

[00:26:04–00:26:12] **Alejandro:** So the transformation has to be top down, and leaders need to adopt, and leaders have to have a very clear plan on what to build.

[00:26:12–00:26:14] **Alejandro:** I've seen so many companies.

[00:26:14–00:26:16] **Alejandro:** It's just like, oh, like, we're doing a hackathon.

[00:26:16–00:26:18] **Alejandro:** People are coming up with use cases.

[00:26:18–00:26:20] **Alejandro:** We're sponsoring some of these use cases.

[00:26:20–00:26:21] **Alejandro:** That doesn't work.

[00:26:21–00:26:30] **Alejandro:** It's like, be very clear on what the company will look like in three or five years, and then start building that.

[00:26:30–00:26:34] **Alejandro:** And be, like, very vertical in guiding your troops towards that.

[00:26:35–00:26:42] **Alejandro:** Like, an army doesn't really work if everyone comes up with ideas on the strategy and tactics and goes to the battlefield and, like, does whatever they want.

[00:26:42–00:26:45] **Alejandro:** Like, you need a very clear strategy, and that's what we need now.

[00:26:46–00:26:47] **Alejandro:** It's at, like, transformation stage.

[00:26:48–00:26:53] **Alejandro:** The second one is you need to measure what really matters, and it's evals, but it's also the right evals.

[00:26:54–00:27:00] **Alejandro:** So I see a lot of companies spending now huge amounts, and they say, okay, I got adoption.

[00:27:00–00:27:04] **Alejandro:** I'm just spending, like, hundreds of millions of dollars in tokens now.

[00:27:04–00:27:05] **Alejandro:** What about that?

[00:27:06–00:27:07] **Alejandro:** Like, there's quality in the tokens.

[00:27:07–00:27:10] **Alejandro:** So I have a framework here that's also useful.

[00:27:11–00:27:21] **Alejandro:** Like, tier three tokens, the most valuable, are these agents where you can get the ROI of each specific token.

[00:27:21–00:27:22] **Alejandro:** And I can do that now.

[00:27:22–00:27:23] **Alejandro:** That's great news for me.

[00:27:24–00:27:32] **Alejandro:** Because I'm growing, and because I know the ROI of each token, because it goes to agents that are performing the job of the organization, right?

[00:27:32–00:27:33] **Alejandro:** These are the best tokens.

[00:27:33–00:27:38] **Alejandro:** Tier two tokens are things that you can measure indirectly.

[00:27:38–00:27:40] **Alejandro:** Do I see devs in the code base?

[00:27:41–00:27:45] **Alejandro:** And I can evaluate the value of these tokens, at least indirectly, and then push those to productions.

[00:27:46–00:27:53] **Alejandro:** Tier one, when most companies are, is people are just using plug code or chat GPT or co-work or whatever.

[00:27:53–00:27:54] **Alejandro:** What happened with those?

[00:27:54–00:27:55] **Alejandro:** I have no idea.

[00:27:56–00:27:57] **Alejandro:** So it's not just about adoption.

[00:27:57–00:28:08] **Alejandro:** It's really about having a very clear vision and then measuring that each token you spend is bringing you those benefits and just iterate, iterate, iterate from there.

[00:28:08–00:28:22] **Host:** And we touched on this a little bit, but I think it's worth a dive as maybe the most ambitious companies listening to this will decide to follow suit, which is you decided to build an agent per customer versus per task.

[00:28:22–00:28:29] **Host:** And then discovered along the way that each one of those agents needs its own micro-virtual machine.

[00:28:29–00:28:33] **Host:** So maybe kind of walk us through those decisions, that architecture.

[00:28:33–00:28:51] **Alejandro:** And I think we're seeing these results now, but it was a really risky bet because people usually go from workflows, like if I could advise everyone, don't build agentic workflows, to graphs or functions or objectives.

[00:28:51–00:28:57] **Alejandro:** And we built that, that these are multi-agent systems that can perform a whole function for a complex goals.

[00:28:58–00:29:04] **Alejandro:** Like the ones I told you that to sell a car, you need to do financing, purchasing, like recommendations, et cetera.

[00:29:05–00:29:11] **Alejandro:** And we had thousands, like tens of thousands of these agents working at scale, running the business back in December.

[00:29:11–00:29:18] **Alejandro:** But then Opus 4.5 came out and I realized like, this isn't the right paradigm anymore.

[00:29:19–00:29:30] **Alejandro:** Like the intelligence now doesn't need like the graph and the multi-agent lattice work and harness because it will constrain this level of intelligence.

[00:29:30–00:29:54] **Alejandro:** So we decided to like destroy everything we had been building for two years that was working, that brought us to profitability, that brought us amazing growth and start over with a harness that we thought would be robust and scalable and leverage recursive self-improvement or new models, more intelligent models coming out every month.

[00:29:54–00:30:08] **Alejandro:** So the way this looks like it's a virtual machine with an agent, with access to memory and evals and the CLI where they can access every tool and every API in my company and the long-term goal.

## 00:30:00–00:35:00

[00:30:09–00:30:17] **Alejandro:** And I instantiate hundreds of thousands of these each day with long-term goals, like maximizing the lifetime value.

[00:30:17–00:30:19] **Alejandro:** The self-improving organization.

[00:30:19–00:30:19] **Host:** Exactly.

[00:30:19–00:30:20] **Alejandro:** The self-improving organization.

[00:30:20–00:30:29] **Alejandro:** And I think people are super obsessed with RSI now, and this will improve the models.

[00:30:30–00:30:41] **Alejandro:** But if you look at it this way, economic value in humanity for the past 4,000 years has been delivered by organization, not by individuals.

[00:30:41–00:30:49] **Alejandro:** So what you want to self-improve and to engage in that loop is the organization that can deliver more economic value, right?

[00:30:49–00:31:13] **Alejandro:** So that's the loop that I think companies will start to focus on because if you get that loop working and it's an organization that is really self-improving and harnessing the newer models and the better intelligence that we're getting every couple of days now, then you hit the exponential, not just in intelligence, but in the value that you can generate as a company.

[00:31:13–00:31:15] **Alejandro:** So that's really exciting.

[00:31:15–00:31:28] **Host:** You mentioned that because of all the challenges in adopting AI, you saw the biggest opportunity on net new companies being formed working on this new way and then disrupting markets.

[00:31:28–00:31:29] **Host:** You want to talk a little bit about that?

[00:31:29–00:31:30] **Alejandro:** Yes.

[00:31:30–00:31:37] **Alejandro:** There's this concept in economics about creative destruction from Joseph Schumpeter.

[00:31:38–00:31:56] **Alejandro:** And what it says is that the way innovation hits the economy isn't by companies adopting the new technology, but by companies remaining the way they were and incumbents with the new technology destroying the old companies.

[00:31:56–00:32:08] **Alejandro:** So this destroys value in the short term in the economy, but in the long term, it's better for everyone because these new, more efficient, more effective companies will provide better products and services for the economy as a whole.

[00:32:08–00:32:13] **Alejandro:** And this has happened in the past industrial revolutions, and this has always happened.

[00:32:13–00:32:23] **Alejandro:** And it's a great opportunity for entrepreneurs and people today because it's hard to adopt AI deeply.

[00:32:24–00:32:32] **Alejandro:** It's really hard for a CEO today, especially of a large company or public company, to go and say, hey, like I'm betting everything on AI.

[00:32:32–00:32:44] **Alejandro:** The company has to look this way, I'll destroy and rebuild everything I've been building for the past 40 years to become an AI native company.

[00:32:45–00:32:48] **Alejandro:** Like how many CEOs will do that in a company at scale?

[00:32:48–00:33:03] **Alejandro:** So while they adopt, new companies can be formed that are built around the strengths of AI and take over and bring new products and services to the masses.

[00:33:04–00:33:06] **Alejandro:** And this has happened before.

[00:33:06–00:33:07] **Alejandro:** Like this happened with electricity.

[00:33:07–00:33:09] **Alejandro:** This is a story I always tell my team.

[00:33:10–00:33:18] **Alejandro:** The technologies for Ford's production line were developed in 1879 and 1881.

[00:33:19–00:33:27] **Alejandro:** Edison started commercializing electricity in New York and then London, and he invented a dynamo that was extremely efficient.

[00:33:27–00:33:34] **Alejandro:** So you could have built Ford's factory 40 years before Ford.

[00:33:35–00:33:35] **Alejandro:** The technology was there.

[00:33:35–00:33:36] **Alejandro:** Everything was there.

[00:33:36–00:33:49] **Alejandro:** But the way people adopted electricity and Ford's dynamo was, okay, I'm going to leave my factory like four floors, shafts and belts, and just change my coal engine for an electric engine.

[00:33:49–00:33:52] **Alejandro:** And this will bring you benefits, yes, but like 6% efficiency.

[00:33:53–00:34:10] **Alejandro:** What needed to be done was to destroy that factory, build it in a flat surface, not in the center of New York, but in Connecticut or New Jersey, and redesign your whole factory around small dynamos and electricity.

[00:34:10–00:34:20] **Alejandro:** And then you get like the 3x improvement in productivity that powered the U.S. during the 20th century.

[00:34:20–00:34:23] **Alejandro:** And the same happened again with the computer, and the same is happening again today.

[00:34:23–00:34:29] **Alejandro:** People want to adopt it, but they're not willing to redesign the whole company, and they just adopt it superficially.

[00:34:29–00:34:37] **Alejandro:** And in the end, that'll give you a 6% or a 10% improvement, not a 10x improvement.

[00:34:37–00:34:43] **Alejandro:** And it's like the innovator's dilemma at an industrial scale again.

[00:34:45–00:34:50] **Host:** I think you've just made an amazing case for any future founders out there that it's time to build.

[00:34:50–00:34:51] **Host:** It's time to build.

[00:34:51–00:34:56] **Host:** And maybe a great place to end is, you know, you've built and scaled your own company.

[00:34:56–00:34:58] **Host:** You've now turned Kavak fully agentic.

[00:34:59–00:35:03] **Host:** Like, what advice do you have to future founders or first-time founders that might be listening?

## 00:35:00–00:40:00

[00:35:04–00:35:07] **Alejandro:** So this is the most exciting time in human history.

[00:35:07–00:35:08] **Alejandro:** I believe that.

[00:35:08–00:35:11] **Alejandro:** Like, we're living in the most exciting time in human history.

[00:35:11–00:35:29] **Alejandro:** And it's the most exciting time to be a founder because it's the first time that anyone has access to the most powerful tools and intelligence in the world, like, almost for free or for $20 a month.

[00:35:29–00:35:38] **Alejandro:** So literally, the democratization of the tools for people to build has never been this way in human history.

[00:35:38–00:35:45] **Alejandro:** And there's so much problems to be solved and a new reality to be built around this new paradigm.

[00:35:46–00:35:49] **Alejandro:** So say, like, just go for it, but go for it deep.

[00:35:50–00:35:53] **Alejandro:** Like, imagine what the future around the AI will look like.

[00:35:54–00:35:57] **Alejandro:** It's not even an exponential.

[00:35:57–00:36:04] **Alejandro:** Just map a trend that's linear if things keep getting, like, AI keeps getting better at a linear scale.

[00:36:04–00:36:11] **Alejandro:** And just build for that, and you'll come up with wonderful ideas that will, like, bring a lot of value to the world.

[00:36:13–00:36:13] **Host:** Amazing.

[00:36:14–00:36:15] **Host:** Ale, thank you for joining us.

[00:36:15–00:36:15] **Alejandro:** Thank you.

[00:36:15–00:36:16] **Alejandro:** Thanks for having me.
