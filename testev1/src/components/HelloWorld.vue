<template>
  <form class="md-layout padding" @submit.prevent="submit">
    <div class="md-layout md-gutter">
      <div class="md-layout-item md-small-size-100">
        <md-field :class="getValidationClass('nome')">
          <label for="nome">Digite um nome para pesquisar</label>
          <md-input name="nome" v-model="form.nome"></md-input>
          <span class="md-error" v-if="!$v.form.nome.required">O campo nome é de preenchimento obrigatório!</span>
          <span class="md-error" v-else-if="!$v.form.nome.minlength">O campo nome deve conter no mínimo 3 caracteres!</span>

        </md-field>

        <md-field>
          <label>Resposta</label>
          <md-textarea disabled v-model="form.textarea"></md-textarea>
        </md-field>

      </div>
    </div>
    <md-button type="submit" class="md-primary">Pesquisar</md-button>
  </form>

</template>

<script>
import { validationMixin } from 'vuelidate'
import {
  required,
  email,
  minLength,
  maxLength
} from 'vuelidate/lib/validators'

export default {
  name: 'CcHelloWorld',

  data () {
    return {
      form: {
        nome: "",
        textarea: "algo"
      }
    }
  },

  validations: {
    form: {
      nome: {
      required,
      minLength: minLength(3)
      }
    }
  },

  methods: {
    getValidationClass (fieldName) {
      const field = this.$v.form[fieldName]

      if (field) {
        return {
          'md-invalid': field.$invalid && field.$dirty
        }
      }
    },

    submit () {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        postApi(this.nome)
      }
    },

    postApi (nome) {
      console.log(nome)
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.padding{
  padding: 15px;
}
</style>
