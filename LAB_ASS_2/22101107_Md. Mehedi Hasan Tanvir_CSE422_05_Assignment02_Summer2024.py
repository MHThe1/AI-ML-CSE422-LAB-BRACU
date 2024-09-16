import random

def get_ranbin(n):
  mylist = ['0', '1']
  strval = ''
  for i in range(n):
    strval += random.choice(mylist)
  return strval

def get_choromosome(n, l):
  chromo_list = []
  for i in range(n):
    chromo_list.append(get_ranbin(l))
  return chromo_list


def fitness(chromo, step, slots):
  div_list = []
  st = 0
  for i in range(slots):
    stop = st+step
    div_list.append(chromo[st:stop])
    st = stop

  penalty = 0
  penalty += overlap_penalty(div_list, step, slots)
  penalty += cons_penalty(div_list, step, slots)
  penalty *= -1

  return penalty

def overlap_penalty(s_chromo, step, slots):
  overlap_penalty = 0
  val = 0
  for i in range(slots):
    val = 0
    for j in range(step):
      val += int(s_chromo[i][j])
    if val != 0:
      overlap_penalty += val - 1
  return(overlap_penalty)

def cons_penalty(s_chromo, step, slots):
  cons_penalty = 0
  val = 0
  for i in range(step):
    val = 0
    for j in range(slots):
      val += int(s_chromo[j][i])
    if val != 0:
      cons_penalty += val - 1
  return(cons_penalty)



def parent_selection(chromosome_list_f):
  chromo1 = random.randrange(0, len(chromosome_list_f))
  chromo2 = random.randrange(0, len(chromosome_list_f))
  while chromo2 == chromo1:
    chromo2 = random.randrange(0, len(chromosome_list_f))
  
  return (chromo1, chromo2)


def single_crossover(child_chromo_list, ch1, ch2):
  point = random.randrange(1, len(ch1)-2)

  ch1_1 = ch1[0:point]
  ch1_2 = ch1[point:len(ch1)]
  ch2_1 = ch2[0:point]
  ch2_2 = ch2[point:len(ch2)]


  child1 = ch1_1+ch2_2
  child2 = ch2_1+ch1_2

  child1_fitness = fitness(child1, 3, 3)
  child2_fitness = fitness(child2, 3, 3)

  if child1_fitness >= child2_fitness:
    child_chromo_list.append(child1)
  else:
    child_chromo_list.append(child2)


def crossover(child_chromo_list, ch1, ch2):
  point1 = random.randrange(0, len(ch1))
  point2 = random.randrange(point1, len(ch1))

  ch1_l = ch1[0:point1]
  ch1_m = ch1[point1:point2]
  ch1_r = ch1[point2:len(ch1)]
  ch2_l = ch2[0:point1]
  ch2_m = ch2[point1:point2]
  ch2_r = ch2[point2:len(ch2)]


  child1 = ch1_l+ch2_m+ch1_r
  child2 = ch2_l+ch1_m+ch2_r

  child1_fitness = fitness(child1, 3, 3)
  child2_fitness = fitness(child2, 3, 3)

  if child1_fitness >= child2_fitness:
    child_chromo_list.append(child1)
  else:
    child_chromo_list.append(child2)


def mutation(child_list):
  mutation_number = random.randrange(1, len(child_list))
  mutated = []
  for i in range(mutation_number):
    mutate_now = random.randrange(1, len(child_list))
    while mutate_now in mutated:
      mutate_now = random.randrange(1, len(child_list))
    mutated.append(mutate_now)

    gene = random.randrange(1, len(child_list[mutate_now]))
    strval = child_list[mutate_now]
    if child_list[mutate_now][gene] == '0':
      child_list[mutate_now] = strval[:gene] + '1' + strval[gene+1:]
    else:
      child_list[mutate_now] = strval[:gene] + '0' + strval[gene+1:]
  
  return child_list


def zeros_condition_check(child):
  total = 0
  for i in range(len(child)):
    total += int(child[i])
  if total==0:
    return True
  else:
    return False


def genetic_algorithm(chromosome_list, n, l):
    child_chromo_list = new_gen(chromosome_list)
    bflag = False
    for i in range(1000):
        for j in range(len(child_chromo_list)):
            child = child_chromo_list[j]
            c_fitness = fitness(child_chromo_list[j], n, l)
            if c_fitness == 0 and zeros_condition_check(child)==False:
                child_found = child
                fitness_found = c_fitness
                bflag = True
        if bflag == True:
            print(child_found)
            print(fitness_found)
            break

        new_gen(child_chromo_list)

    if bflag==False:
        chromosome_list_f = [None]*len(child_chromo_list)
        for i in range(len(child_chromo_list)):
            chromosome_list_f[i] = [child_chromo_list[i], fitness(child_chromo_list[i], n, l)]
        sorted_list = sorted(chromosome_list_f, key=lambda x: x[1], reverse=True)
        print(sorted_list[0][0])
        print(sorted_list[0][1])

def new_gen(chromosome_list):
  child_chromo_list = []
  for i in range(10):
    chromo1, chromo2 = parent_selection(chromosome_list)
    crossover(child_chromo_list, chromosome_list[chromo1], chromosome_list[chromo2])

  child_chromo_list = mutation(child_chromo_list)
  return child_chromo_list


f = open('22101107_Md. Mehedi Hasan Tanvir_CSE422_05_Assignment02_Summer2024_InputFile.txt', 'r')

g_list = []
curr = f.readline().strip()
curr_list = curr.split(" ")
n = int(curr_list[0])
l = int(curr_list[1])
for i in range(n):
  curr = f.readline().strip()
  g_list.append(curr)

f.close()

chromosome_list = get_choromosome(10, n*l)

genetic_algorithm(chromosome_list, n, l)
