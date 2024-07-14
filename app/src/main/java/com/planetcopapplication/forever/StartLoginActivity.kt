package com.planetcopapplication.forever

import android.content.ContentValues.TAG
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContentProviderCompat.requireContext
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInAccount
import com.google.android.gms.auth.api.signin.GoogleSignInClient
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.android.gms.common.api.ApiException
import com.google.android.gms.common.api.Scope
import com.google.android.material.snackbar.Snackbar
import com.google.firebase.Firebase
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.GoogleAuthProvider
import com.google.firebase.auth.auth
import com.planetcopapplication.forever.databinding.ActivityStartLoginBinding
import java.security.AccessController.getContext

//https://firebase.google.com/docs/auth/android/google-signin?hl=ko

const private  val RC_SIGN_IN = 300
class StartLoginActivity : AppCompatActivity() {
    companion object {
        private val TAG = StartLoginActivity::class.java.getSimpleName();
    }
    private lateinit var binding:ActivityStartLoginBinding
    private lateinit var googleAuth: FirebaseAuth
    private lateinit var googleSignInClient: GoogleSignInClient
    private lateinit var startGoogleLoginForResult : ActivityResultLauncher<Intent>
    private lateinit var googleSignInOptions: GoogleSignInOptions
    //출처: https://faith-developer.tistory.com/183 [개발 이야기:티스토리]

    private lateinit var yourToken:String
    //이게 안 좋은 방식인줄은 아는데 이 토큰을 어찌 처리해야 할지 감이 잡히지 않음
    //후에 새 토큰.,만들어볼 예정 아오


    //Google 로그인을 위해 GoogleSignInClient 객체 제작, GoogleSignInOptions 넘겨줌
    private fun getGoogleClient(): GoogleSignInClient {
        val googleSignInOption = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            .requestScopes(Scope("https://www.googleapis.com/auth/pubsub"))
            //.requestServerAuthCode(getString(R.string.google_login_client_id)) // string 파일에 저장해둔 client id 를 이용해 server authcode를 요청한다.
            .requestEmail() // 이메일도 요청할 수 있다.
            .build()

        return GoogleSignIn.getClient(StartLoginActivity(), googleSignInOption)
    }



    fun successLogin(){
        startActivity(Intent(this, MainActivity::class.java))
        finish()
    }
    //출처: https://faith-developer.tistory.com/183 [개발 이야기:티스토리]

    /**
     * =============================
     *  구글 로그인
     *  =============================
     */
    private fun googleSignIn(){
        googleSignInClient.signOut()
        val signInIntent = googleSignInClient.signInIntent
        startActivityForResult(signInIntent, RC_SIGN_IN)
    }


     // GoogleSignInAccount 객체에서 ID 토큰을 가져와서 Firebase 사용자 인증 정보로 교환하고 Firebase 사용자 인증 정보를 사용해 인증.
     private fun firebaseAuthWithGoogle(acct: GoogleSignInAccount) {
         Log.d(TAG, "firebaseAuthWithGoogle:" + acct.id!!)

         val credential = GoogleAuthProvider.getCredential(acct.idToken, null)
         googleAuth.signInWithCredential(credential)
             .addOnCompleteListener(this) { task ->
                 if (task.isSuccessful) {
                     // Sign in success, update UI with the signed-in user's information
                     Log.d(TAG, "signInWithCredential:success")
                     val user = googleAuth.currentUser
                     //updateUI(user)
                 } else {
                     // If sign in fails, display a message to the user.
                     Log.w(TAG, "signInWithCredential:failure", task.exception)
                     //Snackbar.make(main_layout, "Authentication Failed.", Snackbar.LENGTH_SHORT).show()
                     //updateUI(null)
                 }

                 // ...
             }
     }
    //출처: https://faith-developer.tistory.com/183 [개발 이야기:티스토리]


    /**
     * ##########################
     *  Override Method
     * ##########################
     */

    //활동을 초기화할 때 사용자가 현재 로그인되어 있는지 확인합니다
    public override fun onStart() {
        super.onStart()

        val currentUser = googleAuth.currentUser
        //현재 로그인 되어있는지 확인
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityStartLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)




        //initOnClickListener()


        /*
        버튼 관련 프로세스
         */

        var googleLoginBtn = findViewById<Button>(R.id.googleLoginBtn)
        googleLoginBtn.setOnClickListener {
            //구글 로그인을 앱에 통합, GoogleSignInOptions 객체 구성시
            //requestIdToken 호출
            googleSignInOptions = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
                .requestIdToken(yourToken)
                .requestEmail()
                .build()
            googleSignInClient = GoogleSignIn.getClient(this, googleSignInOptions)
            googleAuth = FirebaseAuth.getInstance()
        }

        var mainActivityBtn = findViewById<Button>(R.id.appleLoginBtn)
        mainActivityBtn.setOnClickListener{
            var intent = Intent(applicationContext, MainActivity::class.java)
            startActivity(intent)
        }//메인 퀵스루 버튼

    }

    public override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if (requestCode == RC_SIGN_IN){
            val task = GoogleSignIn.getSignedInAccountFromIntent(data)
            try {
                //Google Sign In was successful, authenticate with Firebase
                val account = task.getResult(ApiException::class.java)
                firebaseAuthWithGoogle(account!!)
            }catch (e: ApiException){
                Log.w(TAG, "Google sign in failed", e)
            }
        }
    }

}