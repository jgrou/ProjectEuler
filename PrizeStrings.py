states = []
limit = 30
ans = 0

def NextAction(current_state='', absent=0, late=0, day=1):
    if day < limit:
        # On time
        new_state = current_state+'O'
        NextAction(new_state, 0, late, day+1)
        
        # Late
        if late == 0:
            new_state = current_state+'L'
            NextAction(new_state, 0, late+1, day+1)
        
        # Absent
        if absent < 2:
            new_state = current_state+'A'
            NextAction(new_state, absent+1, late, day+1)
            
    if day == limit:
        global ans
        # On time
        new_state = current_state+'O'
        ans += 1
        #states.append(new_state)
        
        # Late
        if late == 0:
            new_state = current_state+'L'
            ans += 1
            #states.append(new_state)
        
        # Absent
        if absent < 2:
            new_state = current_state+'A'
            ans += 1
            #states.append(new_state)
            
NextAction()