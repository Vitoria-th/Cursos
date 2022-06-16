class Aluno():
  def __init__(self, nroMatric, nome):   
    self.__nroMatric = nroMatric
    self.__nome = nome
    self.__curso = None
    self.__historico = None

  def getNroMatric(self):
    return self.__nroMatric

  def getCurso(self):
    return self.__curso

  def getNome(self):
    return self.__nome

  def getHistorico(self):
    return self.__historico
  
  def insereCurso(self,curso):
    self.__curso = curso
  
  def criaHistorico(self,historico):
    self.__historico = historico

class Curso():
  def __init__(self, nome, ano):
    self.__nome = nome
    self.__grade = Grade(ano)

  def getNome(self):
    return self.__nome

  def getGrade(self):
    return self.__grade
    
class Historico():
  def __init__(self, aluno):
    self.__discCursadas = []
    self.__aluno = aluno

  def getDiscCursadas(self):
      return self.__discCursadas
  
  def inserirDisc(self,codigo, nome, cargaHoraria):
      Disc = Disciplina(codigo, nome, cargaHoraria)
      self.getDiscCursadas().append(Disc)    
  
  def cargaHorariaTotal(self):
      totalOPT=0    
      totalOBG=0
      var = 0  
      for disc in self.getDiscCursadas():   
        for a in self.__aluno.getCurso().getGrade().getDiscGrade():        
              if disc.getCodigo() == a.getCodigo():
                var=1
                break
              if disc.getCodigo() != a.getCodigo():
                var=0
        if var==1:
          totalOBG = totalOBG + disc.getCargaHoraria()
        else:
          totalOPT = totalOPT + disc.getCargaHoraria() 
      return totalOPT, totalOBG
  
class Grade():
  def __init__(self, ano):
    self.__ano = ano
    self.__discGrade = []

  def getAno(self):
    return self.__ano

  def getDiscGrade(self):
      return self.__discGrade
  
  def inserirDisc(self,codigo, nome, cargaHoraria):
      Disc = Disciplina(codigo, nome, cargaHoraria)
      self.getDiscGrade().append(Disc)

class Disciplina():
  def __init__(self, codigo, nome, cargaHoraria):
    self.__codigo = codigo
    self.__nome = nome
    self.__cargaHoraria = cargaHoraria

  def getCodigo(self):
    return self.__codigo

  def getNome(self):
    return self.__nome
    
  def getCargaHoraria(self):
    return self.__cargaHoraria

if __name__ == "__main__":
  curso1 = Curso("Matemática", 2022)
  curso1.getGrade().inserirDisc( 0, "Fundamentos da Matemática Elementar 1", 64)
  curso1.getGrade().inserirDisc( 1, "Funções", 48)
  curso1.getGrade().inserirDisc( 2, "Matrizes e Geometria Analítica", 48)

  curso2 = Curso("Psicologia",2003)
  curso2.getGrade().inserirDisc(3, "Anatomia", 68)
  curso2.getGrade().inserirDisc(4, "Psicobiologia", 40)
  curso2.getGrade().inserirDisc(5, "Metodologia da Pesquisa;", 40)
  

  aluno1 = Aluno(0, "Lucas")
  
  aluno1.insereCurso(curso1)

  historico1 = Historico(aluno1)
  aluno1.criaHistorico(historico1)
  aluno1.getHistorico().inserirDisc(0, "Fundamentos da Matemática Elementar 1", 64)
  aluno1.getHistorico().inserirDisc(3, "Anatomia", 68)
  aluno1.getHistorico().inserirDisc(4, "Psicobiologia", 40)
  aluno1.getHistorico().inserirDisc(5, "Metodologia da Pesquisa;", 40)
  aluno1.getHistorico().inserirDisc(1, "Funções", 48)

  cargaHora = historico1.cargaHorariaTotal()
  print("Carga horária obrigatória: {} horas \nCarga horária optativa: {} horas".format(cargaHora[1], cargaHora[0]))

  for disc in aluno1.getHistorico().getDiscCursadas():
         print('Código: {}'.format(disc.getCodigo()))
         print('Nome: {}'.format(disc.getNome()))
         print('Carga Horaria: {:.2f}'.format(disc.getCargaHoraria()))
         print()