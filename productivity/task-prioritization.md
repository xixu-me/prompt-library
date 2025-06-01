# Task Prioritization Matrix

## Description

Helps organize and prioritize tasks using various prioritization frameworks like Eisenhower Matrix, MoSCoW method, and value-based scoring. Creates actionable task lists with clear priorities and deadlines.

## Usage

Provide your list of tasks, projects, or initiatives along with relevant context about deadlines, importance, and resources. Specify your preferred prioritization method or let the AI recommend the best approach for your situation.

## Prompt

```markdown
Help me prioritize the following tasks and create an organized action plan:

**Prioritization Context:**
- **Role/Position:** [Your role and responsibilities]
- **Time Frame:** [Daily/Weekly/Monthly planning horizon]
- **Current Workload:** [Current capacity and constraints]
- **Key Goals:** [Main objectives you're working toward]

**Tasks to Prioritize:**
[List all tasks, projects, or initiatives that need prioritization]

For each task, please consider:
- **Urgency:** How time-sensitive is this task?
- **Importance:** How critical is this to your goals?
- **Effort Required:** How much time/energy will this take?
- **Dependencies:** Does this block other work or people?
- **Impact:** What's the potential value or consequence?

**Prioritization Method:**
[Choose one or ask for recommendation]
- **Eisenhower Matrix:** Urgent/Important quadrants
- **MoSCoW Method:** Must have, Should have, Could have, Won't have
- **Value vs. Effort:** High impact, low effort tasks first
- **ICE Score:** Impact, Confidence, Ease scoring
- **Custom Approach:** Based on your specific criteria

**Additional Constraints:**
- **Deadlines:** [Any fixed deadlines or time constraints]
- **Resources:** [Team members, budget, or tool limitations]
- **Dependencies:** [Tasks that depend on others or external factors]
- **Energy Levels:** [When you're most/least productive]

Please provide:
1. **Prioritized Task List** with reasoning for each priority level
2. **Action Plan** with recommended sequence and timing
3. **Quick Wins** that can be completed immediately
4. **Time Blocking Suggestions** for optimal scheduling
5. **Risk Assessment** for high-priority items
6. **Regular Review Schedule** for maintaining priorities

**Personal Preferences:**
[Any specific working styles, preferences, or constraints to consider]
```

## Example Input

```markdown
**Prioritization Context:**
- **Role/Position:** Product Manager at a SaaS startup
- **Time Frame:** Weekly planning (40 hours available)
- **Current Workload:** Managing 3 active projects, regular meetings take 15 hours/week
- **Key Goals:** Launch new feature by end of quarter, improve customer retention, reduce support tickets

**Tasks to Prioritize:**
1. Finalize user research analysis for new dashboard feature
2. Write product requirements document for mobile app
3. Review and respond to 15 customer feedback emails
4. Prepare presentation for next week's board meeting
5. Conduct user interviews for retention study
6. Update project roadmap and timelines
7. Fix critical bug causing payment failures
8. Plan team offsite for next month
9. Review competitor analysis report
10. Optimize onboarding flow based on analytics
11. Schedule 1-on-1s with team members
12. Create documentation for new API endpoints

**Additional Constraints:**
- **Deadlines:** Board presentation due Friday, bug fix needed ASAP
- **Resources:** Engineering team at capacity, limited designer availability
- **Dependencies:** User research needed before finalizing mobile app requirements
- **Energy Levels:** Most focused 9-11 AM, low energy after 3 PM meetings
```

## Example Output

```markdown
# Weekly Task Prioritization Plan

## Priority Classification (Eisenhower Matrix)

### 🚨 Urgent & Important (Do First)
**1. Fix critical bug causing payment failures**
- **Why Priority 1:** Revenue impact, customer trust at risk
- **Time Estimate:** 4-6 hours (coordination with engineering)
- **Action:** Schedule emergency fix session today

**2. Prepare presentation for board meeting**
- **Why Priority 1:** Hard deadline, stakeholder visibility
- **Time Estimate:** 6 hours
- **Action:** Block Thursday morning for focused preparation

### ⭐ Important, Not Urgent (Schedule)
**3. Finalize user research analysis for dashboard feature**
- **Why High Priority:** Blocks Q4 feature development
- **Time Estimate:** 4 hours
- **Action:** Schedule for Tuesday AM (high energy time)

**4. Update project roadmap and timelines**
- **Why High Priority:** Team alignment, board presentation input
- **Time Estimate:** 3 hours
- **Action:** Complete before board presentation

**5. Conduct user interviews for retention study**
- **Why High Priority:** Directly supports retention goal
- **Time Estimate:** 5 hours (including scheduling and prep)
- **Action:** Schedule 3 interviews this week, 2 next week

### ⚡ Urgent, Not Important (Delegate/Minimize)
**6. Review and respond to customer feedback emails**
- **Why Lower Priority:** Important but can be batched
- **Time Estimate:** 2 hours
- **Action:** Batch process Friday afternoon

**7. Schedule 1-on-1s with team members**
- **Why Lower Priority:** Important for team but flexible timing
- **Time Estimate:** 30 minutes scheduling + 3 hours meetings
- **Action:** Delegate scheduling to assistant, do meetings next week

### 📋 Neither Urgent nor Important (Eliminate/Defer)
**8. Plan team offsite for next month**
- **Action:** Defer to next week or delegate to team lead

**9. Review competitor analysis report**
- **Action:** Defer to following week when less urgent items are handled

**10. Create documentation for API endpoints**
- **Action:** Delegate to engineering team or defer

---

## Recommended Weekly Schedule

### Monday (8 hours)
- **9:00-11:00 AM:** Emergency bug fix coordination (2 hours)
- **11:00-12:00 PM:** Project roadmap updates (1 hour)
- **1:00-3:00 PM:** Board presentation outline and data gathering (2 hours)
- **3:00-4:00 PM:** Customer feedback email batch (1 hour)
- **4:00-5:00 PM:** User interview scheduling and prep (1 hour)
- **5:00-5:30 PM:** Quick team check-ins (30 minutes)

### Tuesday (8 hours)
- **9:00-11:00 AM:** 🎯 User research analysis (2 hours - peak focus)
- **11:00-1:00 PM:** Continued user research analysis (2 hours)
- **2:00-4:00 PM:** User interviews (2 hours)
- **4:00-5:00 PM:** Board presentation content development (1 hour)
- **5:00-5:30 PM:** Team standup and priority adjustments (30 minutes)

### Wednesday (8 hours)
- **9:00-12:00 PM:** Board presentation creation and rehearsal (3 hours)
- **1:00-2:00 PM:** Finalize project roadmap updates (1 hour)
- **2:00-4:00 PM:** User interviews (2 hours)
- **4:00-5:00 PM:** Mobile app requirements planning (1 hour)
- **5:00-5:30 PM:** Progress review and Thursday planning (30 minutes)

### Thursday (8 hours)
- **9:00-11:00 AM:** Final board presentation preparation (2 hours)
- **11:00-12:00 PM:** Board presentation rehearsal (1 hour)
- **1:00-3:00 PM:** Board presentation delivery and follow-up (2 hours)
- **3:00-5:00 PM:** Onboarding flow optimization analysis (2 hours)
- **5:00-5:30 PM:** Week wrap-up and Friday planning (30 minutes)

### Friday (8 hours)
- **9:00-11:00 AM:** Mobile app requirements document start (2 hours)
- **11:00-12:00 PM:** Customer feedback email responses (1 hour)
- **1:00-2:00 PM:** 1-on-1 with team lead (1 hour)
- **2:00-4:00 PM:** Week review and next week planning (2 hours)
- **4:00-5:00 PM:** Administrative tasks and cleanup (1 hour)

---

## Quick Wins (Complete This Week)

### ✅ Immediate Actions (< 30 minutes each)
- Email engineering team about bug fix urgency
- Block calendar time for board presentation prep
- Send calendar invites for user interviews
- Update team on priority changes in Slack

### ✅ 1-Hour Actions
- Batch respond to urgent customer emails
- Update project status in management tools
- Schedule next week's 1-on-1 meetings
- Review and prioritize backlog items

---

## Risk Assessment & Mitigation

### High-Risk Items
**1. Bug Fix Complexity**
- **Risk:** May take longer than estimated, affecting other priorities
- **Mitigation:** Involve senior engineer early, prepare communication for stakeholders

**2. Board Presentation Quality**
- **Risk:** Insufficient time for proper preparation
- **Mitigation:** Start with existing templates, focus on key metrics only

**3. User Research Dependencies**
- **Risk:** Interview cancellations could delay analysis
- **Mitigation:** Schedule backup interviews, prepare alternative data sources

---

## Time Blocking Strategy

### Energy-Based Scheduling
- **High Focus Tasks (9-11 AM):** User research analysis, presentation creation
- **Medium Focus Tasks (11 AM-1 PM):** Documentation, planning work
- **Low Focus Tasks (After 3 PM):** Email responses, administrative work
- **Meeting Blocks:** Keep 1-3 PM for interviews and team interactions

### Buffer Time Management
- **Daily Buffer:** 30 minutes at end of each day for unexpected issues
- **Weekly Buffer:** Friday afternoon for catch-up and planning
- **Emergency Reserve:** 2 hours total across the week for critical issues

---

## Success Metrics

### This Week's Goals
- [ ] Critical bug resolved by Wednesday
- [ ] Board presentation delivered successfully
- [ ] User research analysis completed
- [ ] 5 user interviews conducted
- [ ] Project roadmap updated

### Weekly Review Questions
1. Did high-priority items get completed?
2. What caused delays or inefficiencies?
3. How accurate were time estimates?
4. What should be prioritized differently next week?
5. Are we making progress toward quarterly goals?

---

## Next Week Preview

### Priorities to Advance
- Complete mobile app requirements document
- Continue user interviews and retention analysis
- Plan team offsite (delegate to team lead)
- Review competitor analysis
- Start API documentation project

### Schedule Optimization
- Block more focused time for deep work
- Reduce meeting overhead where possible
- Batch similar tasks more effectively
- Build in more buffer time for unexpected priorities

This prioritization framework balances urgent business needs with strategic goals while accounting for your working style and constraints. The key is maintaining flexibility while protecting time for high-impact work.
```

## Variations

- **Daily Planning**: Focus on single-day task management and optimization
- **Project Prioritization**: Prioritize multiple projects or initiatives rather than individual tasks
- **Team Priorities**: Collaborative prioritization for team or department-level work
- **Goal-Based Planning**: Align tasks with specific objectives and key results (OKRs)

## Tips

- Be honest about time estimates - add 25% buffer for most tasks
- Consider your energy levels and schedule demanding work during peak hours
- Review and adjust priorities regularly as circumstances change
- Don't overcommit - it's better to do fewer things well
- Include time for unexpected urgent tasks in your planning
- Use the 2-minute rule: if something takes less than 2 minutes, do it immediately

## Related Prompts

- `meeting-summary.md` - For capturing action items from meetings to prioritize
- `email-templates.md` - For communicating priorities and deadlines
- `brainstorming-session.md` - For generating solutions to productivity challenges

## Tags

`productivity` `time-management` `prioritization` `planning` `organization` `task-management`
