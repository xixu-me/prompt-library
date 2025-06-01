# Meeting Summary Generator

## Description

Creates comprehensive meeting summaries including key decisions, action items, attendee information, and follow-up tasks. Transforms meeting notes or recordings into structured, actionable summaries that can be distributed to stakeholders.

## Usage

Provide meeting notes, transcript, or key discussion points. Include meeting context, attendees, and any specific format requirements. Works for various meeting types including status updates, planning sessions, client meetings, and board meetings.

## Prompt

```markdown
Create a comprehensive meeting summary from the following information:

**Meeting Details:**
- **Date & Time:** [Meeting date and duration]
- **Meeting Type:** [Status update / Planning / Client meeting / Board meeting / Other]
- **Attendees:** [List of participants and their roles]
- **Meeting Purpose:** [Primary objective of the meeting]

**Meeting Content:**
[Provide meeting notes, transcript, or key discussion points here]

**Summary Requirements:**
- **Format:** [Email summary / Document / Bullet points / Detailed report]
- **Target Audience:** [Team members / Executives / Clients / All attendees]
- **Length:** [Brief overview / Detailed summary / Comprehensive report]
- **Follow-up needs:** [Action items tracking / Next meeting scheduling / Progress monitoring]

Please structure the summary with:

1. **Meeting Overview**
   - Purpose and context
   - Key attendees and their roles
   - Meeting duration and format

2. **Key Decisions Made**
   - Important resolutions and agreements
   - Approved proposals or changes
   - Rejected or deferred items

3. **Discussion Highlights**
   - Main topics covered
   - Different viewpoints presented
   - Concerns or challenges raised

4. **Action Items**
   - Specific tasks assigned
   - Responsible parties
   - Due dates and deadlines
   - Success criteria

5. **Next Steps**
   - Follow-up meetings scheduled
   - Dependencies and blockers
   - Escalation needs

6. **Parking Lot**
   - Topics to revisit later
   - Ideas for future consideration
   - Unresolved questions

**Additional Requirements:**
[Any specific formatting, distribution lists, or follow-up protocols]
```

## Example Input

```markdown
**Meeting Details:**
- **Date & Time:** March 15, 2024, 2:00-3:30 PM EST
- **Meeting Type:** Quarterly Planning Session
- **Attendees:** 
  - Sarah Chen (Product Manager)
  - Mike Rodriguez (Engineering Lead)
  - Alex Kim (Marketing Director)
  - Jordan Thompson (Sales Manager)
  - Chris Wong (Designer)
- **Meeting Purpose:** Plan Q2 product roadmap and marketing initiatives

**Meeting Content:**
Sarah opened by reviewing Q1 performance - exceeded user growth by 15% but behind on revenue targets. Mike discussed technical debt issues affecting new feature development timeline. Alex presented market research showing demand for mobile app priority. Jordan shared feedback from enterprise clients requesting advanced analytics. Chris showed new UI designs for dashboard redesign. 

Key discussions:
- Should we prioritize mobile app development or dashboard redesign?
- Technical debt cleanup will require 3 weeks of dev time
- Enterprise analytics feature could bring $200K ARR but needs 2 month dev time
- Marketing budget increase needed for Q2 campaign
- Hiring 2 more developers by end of Q2

Decisions made:
- Move forward with dashboard redesign in April
- Delay mobile app to Q3
- Allocate 3 weeks in early April for technical debt
- Approve additional $50K marketing budget
- Start hiring process for 2 developers immediately

Action items discussed:
Sarah to update product roadmap by March 20
Mike to create technical debt cleanup plan
Alex to draft Q2 marketing campaign proposal
Jordan to gather detailed enterprise requirements
Chris to finalize dashboard designs
```

## Example Output

```markdown
# Q2 Planning Meeting Summary

**Meeting Date:** March 15, 2024 | **Duration:** 1.5 hours  
**Meeting Type:** Quarterly Planning Session  
**Meeting Lead:** Sarah Chen (Product Manager)

## Attendees
- **Sarah Chen** - Product Manager (Meeting Lead)
- **Mike Rodriguez** - Engineering Lead
- **Alex Kim** - Marketing Director  
- **Jordan Thompson** - Sales Manager
- **Chris Wong** - Designer

---

## Meeting Overview

The team convened to establish Q2 priorities based on Q1 performance and market opportunities. While user growth exceeded targets by 15%, revenue targets were missed, prompting a strategic review of product and marketing initiatives.

---

## Key Decisions Made

### ✅ **Approved Initiatives**
1. **Dashboard Redesign Priority** - Proceed with dashboard redesign in April over mobile app development
2. **Technical Debt Resolution** - Allocate 3 weeks in early April for technical debt cleanup
3. **Marketing Budget Increase** - Approve additional $50K for Q2 marketing campaigns
4. **Team Expansion** - Begin immediate hiring process for 2 additional developers

### ❌ **Deferred Items**
- **Mobile App Development** - Postponed to Q3 to focus on core platform improvements

---

## Discussion Highlights

### Q1 Performance Review
- **Positive:** User growth exceeded targets by 15%
- **Challenge:** Revenue targets not met, requiring strategic adjustment

### Technical Considerations
- Technical debt issues identified as blocking factor for new feature development
- 3-week cleanup period required before major new development
- Engineering capacity constraints affecting timeline

### Market Opportunities
- Market research indicates strong demand for mobile app capabilities
- Enterprise clients requesting advanced analytics features
- Potential $200K ARR from enterprise analytics (2-month development required)

### Resource Requirements
- Additional marketing budget needed to capitalize on Q2 opportunities
- Engineering team expansion critical for meeting Q2-Q3 roadmap

---

## Action Items

| Task | Owner | Due Date | Status |
|------|-------|----------|---------|
| Update product roadmap with Q2 priorities | Sarah Chen | March 20, 2024 | 🔄 In Progress |
| Create technical debt cleanup plan with timeline | Mike Rodriguez | March 22, 2024 | 📋 Assigned |
| Draft Q2 marketing campaign proposal | Alex Kim | March 25, 2024 | 📋 Assigned |
| Gather detailed enterprise analytics requirements | Jordan Thompson | March 27, 2024 | 📋 Assigned |
| Finalize dashboard redesign mockups | Chris Wong | March 20, 2024 | 🔄 In Progress |
| Post job descriptions for developer positions | Sarah Chen | March 18, 2024 | 📋 Assigned |

---

## Next Steps

### Immediate Priorities (Next 2 Weeks)
- Complete Q2 roadmap documentation
- Finalize technical debt cleanup plan
- Begin developer recruitment process

### Q2 Execution Plan
- **April Week 1-3:** Technical debt cleanup
- **April Week 4:** Begin dashboard redesign development
- **May-June:** Dashboard redesign completion and testing

### Follow-up Meetings
- **Weekly standups** every Monday at 10 AM
- **Next planning session** scheduled for April 15, 2024
- **Q2 review meeting** scheduled for June 30, 2024

---

## Parking Lot Items

### Future Consideration
- **Mobile App Development** - Revisit for Q3 planning
- **Enterprise Analytics Suite** - Evaluate after developer hiring complete
- **International Market Expansion** - Research for Q4 planning

### Unresolved Questions
- Budget allocation for potential enterprise analytics development
- Timeline for Q3 mobile app development kickoff
- Long-term hiring plan beyond Q2 additions

---

## Meeting Effectiveness
- ✅ All key decisions made within scheduled time
- ✅ Clear action items assigned with deadlines
- ✅ Resource conflicts identified and resolved
- 📝 Follow-up: Distribute updated roadmap to stakeholders by March 21

---

*Summary prepared by: Sarah Chen*  
*Distribution: All attendees + Executive Team*  
*Next Meeting: April 15, 2024, 2:00 PM EST*
```

## Variations

- **Client Meeting Summary**: Focus on client needs, proposals, and relationship management
- **Technical Review**: Emphasize technical decisions, architecture, and implementation details
- **Executive Brief**: High-level summary for leadership with key metrics and decisions
- **Project Status**: Focus on project milestones, risks, and resource allocation

## Tips

- Capture decisions separately from discussions to highlight outcomes
- Use clear formatting with headers and bullet points for easy scanning
- Include specific deadlines and ownership for all action items
- Note any dependencies or blockers that could affect timelines
- Distribute summaries within 24 hours of the meeting
- Keep a consistent format for regular meeting types

## Related Prompts

- `email-templates.md` - For distributing meeting summaries via email
- `proposal-writer.md` - For creating detailed proposals from meeting discussions
- `technical-documentation.md` - For documenting technical decisions from meetings

## Tags

`meeting-management` `business-communication` `project-management` `documentation` `follow-up` `action-items`
